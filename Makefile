PROJECT_NAME := Amazon Web Services (AWS) Package
include build/common.mk

PACK             := aws
PACKDIR          := sdk
PROJECT          := github.com/pulumi/pulumi-aws

TFGEN           := pulumi-tfgen-${PACK}
PROVIDER        := pulumi-resource-${PACK}
VERSION         := $(shell scripts/get-version)
PYPI_VERSION    := $(shell scripts/get-py-version)

GOMETALINTERBIN=gometalinter
GOMETALINTER=${GOMETALINTERBIN} --config=Gometalinter.json

TESTPARALLELISM := 4

# NOTE: Since the plugin is published using the nodejs style semver version
# We set the PLUGIN_VERSION to be the same as the version we use when building
# the provider (e.g. x.y.z-dev-... instead of x.y.zdev...)
build::
	go install -ldflags "-X github.com/pulumi/pulumi-aws/pkg/version.Version=${VERSION}" ${PROJECT}/cmd/${TFGEN}
	go install -ldflags "-X github.com/pulumi/pulumi-aws/pkg/version.Version=${VERSION}" ${PROJECT}/cmd/${PROVIDER}
	for LANGUAGE in "nodejs" "python" "go" ; do \
		$(TFGEN) $$LANGUAGE --overlays overlays/$$LANGUAGE/ --out ${PACKDIR}/$$LANGUAGE/ || exit 3 ; \
	done
	cd ${PACKDIR}/nodejs/ && \
		yarn install && \
		yarn run tsc && \
		cp ../../README.md ../../LICENSE package.json yarn.lock ./bin/ && \
		sed -i.bak "s/\$${VERSION}/$(VERSION)/g" ./bin/package.json && \
		cd bin/ && \
			cp ../yarn.lock . && \
			(yarn unlink > /dev/null 2>&1 || true) && \
			yarn link && \
			yarn install --offline --production

	cd ${PACKDIR}/python/ && \
		if [ $$(command -v pandoc) ]; then \
			pandoc --from=markdown --to=rst --output=README.rst ../../README.md; \
		else \
			echo "warning: pandoc not found, not generating README.rst"; \
			echo "" > README.rst; \
		fi && \
		$(PYTHON) setup.py clean --all 2>/dev/null && \
		rm -rf ./bin/ ../python.bin/ && cp -R . ../python.bin && mv ../python.bin ./bin && \
		sed -i.bak -e "s/\$${VERSION}/$(PYPI_VERSION)/g" -e "s/\$${PLUGIN_VERSION}/$(VERSION)/g" ./bin/setup.py && \
		rm ./bin/setup.py.bak && \
		cd ./bin && $(PYTHON) setup.py build sdist && $(PIP) install --user -e .

lint::
	$(GOMETALINTER) ./cmd/... resources.go | sort ; exit "$${PIPESTATUS[0]}"

test_all::
	PATH=$(PULUMI_BIN):$(PATH) go test -v -cover -timeout 1h -parallel ${TESTPARALLELISM} ./examples
	PATH=$(PULUMI_BIN):$(PATH) go test -v -cover -timeout 1h -parallel ${TESTPARALLELISM} ./tests/...

.PHONY: publish_tgz
publish_tgz:
	$(call STEP_MESSAGE)
	./scripts/publish_tgz.sh

.PHONY: publish_packages
publish_packages:
	$(call STEP_MESSAGE)
	./scripts/publish_packages.sh

.PHONY: check_clean_worktree
check_clean_worktree:
	$$(go env GOPATH)/src/github.com/pulumi/scripts/ci/check-worktree-is-clean.sh

# The travis_* targets are entrypoints for CI.
.PHONY: travis_cron travis_push travis_pull_request travis_api
travis_cron: all
travis_push: only_build check_clean_worktree publish_tgz only_test publish_packages
travis_pull_request: all check_clean_worktree
travis_api: all
