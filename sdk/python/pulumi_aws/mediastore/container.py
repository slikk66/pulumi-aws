# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class Container(pulumi.CustomResource):
    """
    Provides a MediaStore Container.
    """
    def __init__(__self__, __name__, __opts__=None, name=None):
        """Create a Container resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        The name of the container. Must contain alphanumeric characters or underscores.
        """
        __props__['name'] = name

        __self__.arn = pulumi.runtime.UNKNOWN
        """
        The ARN of the container.
        """
        __self__.endpoint = pulumi.runtime.UNKNOWN
        """
        The DNS endpoint of the container.
        """

        super(Container, __self__).__init__(
            'aws:mediastore/container:Container',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'arn' in outs:
            self.arn = outs['arn']
        if 'endpoint' in outs:
            self.endpoint = outs['endpoint']
        if 'name' in outs:
            self.name = outs['name']
