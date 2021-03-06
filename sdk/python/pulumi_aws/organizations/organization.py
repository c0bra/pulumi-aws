# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class Organization(pulumi.CustomResource):
    """
    Provides a resource to create an organization.
    """
    def __init__(__self__, __name__, __opts__=None, feature_set=None):
        """Create a Organization resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if feature_set and not isinstance(feature_set, basestring):
            raise TypeError('Expected property feature_set to be a basestring')
        __self__.feature_set = feature_set
        """
        Specify "ALL" (default) or "CONSOLIDATED_BILLING".
        """
        __props__['featureSet'] = feature_set

        __self__.arn = pulumi.runtime.UNKNOWN
        """
        ARN of the organization
        """
        __self__.master_account_arn = pulumi.runtime.UNKNOWN
        """
        ARN of the master account
        """
        __self__.master_account_email = pulumi.runtime.UNKNOWN
        """
        Email address of the master account
        """
        __self__.master_account_id = pulumi.runtime.UNKNOWN
        """
        Identifier of the master account
        """

        super(Organization, __self__).__init__(
            'aws:organizations/organization:Organization',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'arn' in outs:
            self.arn = outs['arn']
        if 'featureSet' in outs:
            self.feature_set = outs['featureSet']
        if 'masterAccountArn' in outs:
            self.master_account_arn = outs['masterAccountArn']
        if 'masterAccountEmail' in outs:
            self.master_account_email = outs['masterAccountEmail']
        if 'masterAccountId' in outs:
            self.master_account_id = outs['masterAccountId']
