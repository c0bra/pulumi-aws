# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class Pipeline(pulumi.CustomResource):
    """
    Provides an Elastic Transcoder pipeline resource.
    """
    def __init__(__self__, __name__, __opts__=None, aws_kms_key_arn=None, content_config=None, content_config_permissions=None, input_bucket=None, name=None, notifications=None, output_bucket=None, role=None, thumbnail_config=None, thumbnail_config_permissions=None):
        """Create a Pipeline resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if aws_kms_key_arn and not isinstance(aws_kms_key_arn, basestring):
            raise TypeError('Expected property aws_kms_key_arn to be a basestring')
        __self__.aws_kms_key_arn = aws_kms_key_arn
        """
        The AWS Key Management Service (AWS KMS) key that you want to use with this pipeline.
        """
        __props__['awsKmsKeyArn'] = aws_kms_key_arn

        if content_config and not isinstance(content_config, dict):
            raise TypeError('Expected property content_config to be a dict')
        __self__.content_config = content_config
        """
        The ContentConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists. (documented below)
        """
        __props__['contentConfig'] = content_config

        if content_config_permissions and not isinstance(content_config_permissions, list):
            raise TypeError('Expected property content_config_permissions to be a list')
        __self__.content_config_permissions = content_config_permissions
        """
        The permissions for the `content_config` object. (documented below)
        """
        __props__['contentConfigPermissions'] = content_config_permissions

        if not input_bucket:
            raise TypeError('Missing required property input_bucket')
        elif not isinstance(input_bucket, basestring):
            raise TypeError('Expected property input_bucket to be a basestring')
        __self__.input_bucket = input_bucket
        """
        The Amazon S3 bucket in which you saved the media files that you want to transcode and the graphics that you want to use as watermarks.
        """
        __props__['inputBucket'] = input_bucket

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        The name of the pipeline. Maximum 40 characters
        """
        __props__['name'] = name

        if notifications and not isinstance(notifications, dict):
            raise TypeError('Expected property notifications to be a dict')
        __self__.notifications = notifications
        """
        The Amazon Simple Notification Service (Amazon SNS) topic that you want to notify to report job status. (documented below)
        """
        __props__['notifications'] = notifications

        if output_bucket and not isinstance(output_bucket, basestring):
            raise TypeError('Expected property output_bucket to be a basestring')
        __self__.output_bucket = output_bucket
        """
        The Amazon S3 bucket in which you want Elastic Transcoder to save the transcoded files.
        """
        __props__['outputBucket'] = output_bucket

        if not role:
            raise TypeError('Missing required property role')
        elif not isinstance(role, basestring):
            raise TypeError('Expected property role to be a basestring')
        __self__.role = role
        """
        The IAM Amazon Resource Name (ARN) for the role that you want Elastic Transcoder to use to transcode jobs for this pipeline.
        """
        __props__['role'] = role

        if thumbnail_config and not isinstance(thumbnail_config, dict):
            raise TypeError('Expected property thumbnail_config to be a dict')
        __self__.thumbnail_config = thumbnail_config
        """
        The ThumbnailConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files. (documented below)
        """
        __props__['thumbnailConfig'] = thumbnail_config

        if thumbnail_config_permissions and not isinstance(thumbnail_config_permissions, list):
            raise TypeError('Expected property thumbnail_config_permissions to be a list')
        __self__.thumbnail_config_permissions = thumbnail_config_permissions
        """
        The permissions for the `thumbnail_config` object. (documented below)
        """
        __props__['thumbnailConfigPermissions'] = thumbnail_config_permissions

        __self__.arn = pulumi.runtime.UNKNOWN

        super(Pipeline, __self__).__init__(
            'aws:elastictranscoder/pipeline:Pipeline',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'arn' in outs:
            self.arn = outs['arn']
        if 'awsKmsKeyArn' in outs:
            self.aws_kms_key_arn = outs['awsKmsKeyArn']
        if 'contentConfig' in outs:
            self.content_config = outs['contentConfig']
        if 'contentConfigPermissions' in outs:
            self.content_config_permissions = outs['contentConfigPermissions']
        if 'inputBucket' in outs:
            self.input_bucket = outs['inputBucket']
        if 'name' in outs:
            self.name = outs['name']
        if 'notifications' in outs:
            self.notifications = outs['notifications']
        if 'outputBucket' in outs:
            self.output_bucket = outs['outputBucket']
        if 'role' in outs:
            self.role = outs['role']
        if 'thumbnailConfig' in outs:
            self.thumbnail_config = outs['thumbnailConfig']
        if 'thumbnailConfigPermissions' in outs:
            self.thumbnail_config_permissions = outs['thumbnailConfigPermissions']
