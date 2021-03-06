# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class AccessKey(pulumi.CustomResource):
    """
    Provides an IAM access key. This is a set of credentials that allow API requests to be made as an IAM user.
    """
    def __init__(__self__, __name__, __opts__=None, pgp_key=None, user=None):
        """Create a AccessKey resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if pgp_key and not isinstance(pgp_key, basestring):
            raise TypeError('Expected property pgp_key to be a basestring')
        __self__.pgp_key = pgp_key
        """
        Either a base-64 encoded PGP public key, or a
        keybase username in the form `keybase:some_person_that_exists`.
        """
        __props__['pgpKey'] = pgp_key

        if not user:
            raise TypeError('Missing required property user')
        elif not isinstance(user, basestring):
            raise TypeError('Expected property user to be a basestring')
        __self__.user = user
        """
        The IAM user to associate with this access key.
        """
        __props__['user'] = user

        __self__.encrypted_secret = pulumi.runtime.UNKNOWN
        """
        The encrypted secret, base64 encoded.
        ~> **NOTE:** The encrypted secret may be decrypted using the command line,
        for example: `terraform output encrypted_secret | base64 --decode | keybase pgp decrypt`.
        """
        __self__.key_fingerprint = pulumi.runtime.UNKNOWN
        """
        The fingerprint of the PGP key used to encrypt
        the secret
        """
        __self__.secret = pulumi.runtime.UNKNOWN
        """
        The secret access key. Note that this will be written
        to the state file. Please supply a `pgp_key` instead, which will prevent the
        secret from being stored in plain text
        """
        __self__.ses_smtp_password = pulumi.runtime.UNKNOWN
        """
        The secret access key converted into an SES SMTP
        password by applying [AWS's documented conversion
        algorithm](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/smtp-credentials.html#smtp-credentials-convert).
        """
        __self__.status = pulumi.runtime.UNKNOWN
        """
        "Active" or "Inactive". Keys are initially active, but can be made
        inactive by other means.
        """

        super(AccessKey, __self__).__init__(
            'aws:iam/accessKey:AccessKey',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'encryptedSecret' in outs:
            self.encrypted_secret = outs['encryptedSecret']
        if 'keyFingerprint' in outs:
            self.key_fingerprint = outs['keyFingerprint']
        if 'pgpKey' in outs:
            self.pgp_key = outs['pgpKey']
        if 'secret' in outs:
            self.secret = outs['secret']
        if 'sesSmtpPassword' in outs:
            self.ses_smtp_password = outs['sesSmtpPassword']
        if 'status' in outs:
            self.status = outs['status']
        if 'user' in outs:
            self.user = outs['user']
