# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class Rule(pulumi.CustomResource):
    """
    Provides an WAF Regional Rule Resource for use with Application Load Balancer.
    """
    def __init__(__self__, __name__, __opts__=None, metric_name=None, name=None, predicates=None):
        """Create a Rule resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not metric_name:
            raise TypeError('Missing required property metric_name')
        elif not isinstance(metric_name, basestring):
            raise TypeError('Expected property metric_name to be a basestring')
        __self__.metric_name = metric_name
        """
        The name or description for the Amazon CloudWatch metric of this rule.
        """
        __props__['metricName'] = metric_name

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        The name or description of the rule.
        """
        __props__['name'] = name

        if predicates and not isinstance(predicates, list):
            raise TypeError('Expected property predicates to be a list')
        __self__.predicates = predicates
        """
        The objects to include in a rule.
        """
        __props__['predicates'] = predicates

        super(Rule, __self__).__init__(
            'aws:wafregional/rule:Rule',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'metricName' in outs:
            self.metric_name = outs['metricName']
        if 'name' in outs:
            self.name = outs['name']
        if 'predicates' in outs:
            self.predicates = outs['predicates']
