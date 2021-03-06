# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class TaskDefinition(pulumi.CustomResource):
    """
    Manages a revision of an ECS task definition to be used in `aws_ecs_service`.
    """
    def __init__(__self__, __name__, __opts__=None, container_definitions=None, cpu=None, execution_role_arn=None, family=None, memory=None, network_mode=None, placement_constraints=None, requires_compatibilities=None, task_role_arn=None, volumes=None):
        """Create a TaskDefinition resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not container_definitions:
            raise TypeError('Missing required property container_definitions')
        elif not isinstance(container_definitions, basestring):
            raise TypeError('Expected property container_definitions to be a basestring')
        __self__.container_definitions = container_definitions
        """
        A list of valid [container definitions]
        (http://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html) provided as a
        single valid JSON document. Please note that you should only provide values that are part of the container
        definition document. For a detailed description of what parameters are available, see the [Task Definition Parameters]
        (https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html) section from the
        official [Developer Guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide).
        """
        __props__['containerDefinitions'] = container_definitions

        if cpu and not isinstance(cpu, basestring):
            raise TypeError('Expected property cpu to be a basestring')
        __self__.cpu = cpu
        """
        The number of cpu units used by the task. If the `requires_compatibilities` is `FARGATE` this field is required.
        """
        __props__['cpu'] = cpu

        if execution_role_arn and not isinstance(execution_role_arn, basestring):
            raise TypeError('Expected property execution_role_arn to be a basestring')
        __self__.execution_role_arn = execution_role_arn
        """
        The Amazon Resource Name (ARN) of the task execution role that the Amazon ECS container agent and the Docker daemon can assume.
        """
        __props__['executionRoleArn'] = execution_role_arn

        if not family:
            raise TypeError('Missing required property family')
        elif not isinstance(family, basestring):
            raise TypeError('Expected property family to be a basestring')
        __self__.family = family
        """
        A unique name for your task definition.
        """
        __props__['family'] = family

        if memory and not isinstance(memory, basestring):
            raise TypeError('Expected property memory to be a basestring')
        __self__.memory = memory
        """
        The amount (in MiB) of memory used by the task. If the `requires_compatibilities` is `FARGATE` this field is required.
        """
        __props__['memory'] = memory

        if network_mode and not isinstance(network_mode, basestring):
            raise TypeError('Expected property network_mode to be a basestring')
        __self__.network_mode = network_mode
        """
        The Docker networking mode to use for the containers in the task. The valid values are `none`, `bridge`, `awsvpc`, and `host`.
        """
        __props__['networkMode'] = network_mode

        if placement_constraints and not isinstance(placement_constraints, list):
            raise TypeError('Expected property placement_constraints to be a list')
        __self__.placement_constraints = placement_constraints
        """
        A set of placement constraints rules that are taken into consideration during task placement. Maximum number of `placement_constraints` is `10`.
        """
        __props__['placementConstraints'] = placement_constraints

        if requires_compatibilities and not isinstance(requires_compatibilities, list):
            raise TypeError('Expected property requires_compatibilities to be a list')
        __self__.requires_compatibilities = requires_compatibilities
        """
        A set of launch types required by the task. The valid values are `EC2` and `FARGATE`.
        """
        __props__['requiresCompatibilities'] = requires_compatibilities

        if task_role_arn and not isinstance(task_role_arn, basestring):
            raise TypeError('Expected property task_role_arn to be a basestring')
        __self__.task_role_arn = task_role_arn
        """
        The ARN of IAM role that allows your Amazon ECS container task to make calls to other AWS services.
        """
        __props__['taskRoleArn'] = task_role_arn

        if volumes and not isinstance(volumes, list):
            raise TypeError('Expected property volumes to be a list')
        __self__.volumes = volumes
        """
        A set of volume blocks that containers in your task may use.
        """
        __props__['volumes'] = volumes

        __self__.arn = pulumi.runtime.UNKNOWN
        """
        Full ARN of the Task Definition (including both `family` and `revision`).
        """
        __self__.revision = pulumi.runtime.UNKNOWN
        """
        The revision of the task in a particular family.
        """

        super(TaskDefinition, __self__).__init__(
            'aws:ecs/taskDefinition:TaskDefinition',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'arn' in outs:
            self.arn = outs['arn']
        if 'containerDefinitions' in outs:
            self.container_definitions = outs['containerDefinitions']
        if 'cpu' in outs:
            self.cpu = outs['cpu']
        if 'executionRoleArn' in outs:
            self.execution_role_arn = outs['executionRoleArn']
        if 'family' in outs:
            self.family = outs['family']
        if 'memory' in outs:
            self.memory = outs['memory']
        if 'networkMode' in outs:
            self.network_mode = outs['networkMode']
        if 'placementConstraints' in outs:
            self.placement_constraints = outs['placementConstraints']
        if 'requiresCompatibilities' in outs:
            self.requires_compatibilities = outs['requiresCompatibilities']
        if 'revision' in outs:
            self.revision = outs['revision']
        if 'taskRoleArn' in outs:
            self.task_role_arn = outs['taskRoleArn']
        if 'volumes' in outs:
            self.volumes = outs['volumes']
