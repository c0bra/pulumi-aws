# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class QueuePolicy(pulumi.CustomResource):
    """
    Allows you to set a policy of an SQS Queue
    while referencing ARN of the queue within the policy.
    """
    def __init__(__self__, __name__, __opts__=None, policy=None, queue_url=None):
        """Create a QueuePolicy resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not policy:
            raise TypeError('Missing required property policy')
        elif not isinstance(policy, basestring):
            raise TypeError('Expected property policy to be a basestring')
        __self__.policy = policy
        """
        The JSON policy for the SQS queue. For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html).
        """
        __props__['policy'] = policy

        if not queue_url:
            raise TypeError('Missing required property queue_url')
        elif not isinstance(queue_url, basestring):
            raise TypeError('Expected property queue_url to be a basestring')
        __self__.queue_url = queue_url
        """
        The URL of the SQS Queue to which to attach the policy
        """
        __props__['queueUrl'] = queue_url

        super(QueuePolicy, __self__).__init__(
            'aws:sqs/queuePolicy:QueuePolicy',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'policy' in outs:
            self.policy = outs['policy']
        if 'queueUrl' in outs:
            self.queue_url = outs['queueUrl']
