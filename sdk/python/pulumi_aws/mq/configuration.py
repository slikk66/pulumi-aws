# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class Configuration(pulumi.CustomResource):
    """
    Provides an MQ Configuration Resource. 
    
    For more information on Amazon MQ, see [Amazon MQ documentation](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/welcome.html).
    """
    def __init__(__self__, __name__, __opts__=None, data=None, description=None, engine_type=None, engine_version=None, name=None):
        """Create a Configuration resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not data:
            raise TypeError('Missing required property data')
        elif not isinstance(data, basestring):
            raise TypeError('Expected property data to be a basestring')
        __self__.data = data
        """
        The broker configuration in XML format.
        See [official docs](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-broker-configuration-parameters.html)
        for supported parameters and format of the XML.
        """
        __props__['data'] = data

        if description and not isinstance(description, basestring):
            raise TypeError('Expected property description to be a basestring')
        __self__.description = description
        """
        The description of the configuration.
        """
        __props__['description'] = description

        if not engine_type:
            raise TypeError('Missing required property engine_type')
        elif not isinstance(engine_type, basestring):
            raise TypeError('Expected property engine_type to be a basestring')
        __self__.engine_type = engine_type
        """
        The type of broker engine.
        """
        __props__['engineType'] = engine_type

        if not engine_version:
            raise TypeError('Missing required property engine_version')
        elif not isinstance(engine_version, basestring):
            raise TypeError('Expected property engine_version to be a basestring')
        __self__.engine_version = engine_version
        """
        The version of the broker engine.
        """
        __props__['engineVersion'] = engine_version

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        The name of the configuration
        """
        __props__['name'] = name

        __self__.arn = pulumi.runtime.UNKNOWN
        """
        The ARN of the configuration.
        """
        __self__.latest_revision = pulumi.runtime.UNKNOWN
        """
        The latest revision of the configuration.
        """

        super(Configuration, __self__).__init__(
            'aws:mq/configuration:Configuration',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'arn' in outs:
            self.arn = outs['arn']
        if 'data' in outs:
            self.data = outs['data']
        if 'description' in outs:
            self.description = outs['description']
        if 'engineType' in outs:
            self.engine_type = outs['engineType']
        if 'engineVersion' in outs:
            self.engine_version = outs['engineVersion']
        if 'latestRevision' in outs:
            self.latest_revision = outs['latestRevision']
        if 'name' in outs:
            self.name = outs['name']
