# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class LoadBalancer(pulumi.CustomResource):
    """
    Provides a Load Balancer resource.
    
    ~> **Note:** `aws_alb` is known as `aws_lb`. The functionality is identical.
    """
    def __init__(__self__, __name__, __opts__=None, access_logs=None, enable_cross_zone_load_balancing=None, enable_deletion_protection=None, enable_http2=None, idle_timeout=None, internal=None, ip_address_type=None, load_balancer_type=None, name=None, name_prefix=None, security_groups=None, subnet_mappings=None, subnets=None, tags=None):
        """Create a LoadBalancer resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if access_logs and not isinstance(access_logs, dict):
            raise TypeError('Expected property access_logs to be a dict')
        __self__.access_logs = access_logs
        """
        An Access Logs block. Access Logs documented below. Only valid for Load Balancers of type `application`.
        """
        __props__['accessLogs'] = access_logs

        if enable_cross_zone_load_balancing and not isinstance(enable_cross_zone_load_balancing, bool):
            raise TypeError('Expected property enable_cross_zone_load_balancing to be a bool')
        __self__.enable_cross_zone_load_balancing = enable_cross_zone_load_balancing
        """
        If true, cross-zone load balancing of the load balancer will be enabled.
        This is a `network` load balancer feature. Defaults to `false`.
        """
        __props__['enableCrossZoneLoadBalancing'] = enable_cross_zone_load_balancing

        if enable_deletion_protection and not isinstance(enable_deletion_protection, bool):
            raise TypeError('Expected property enable_deletion_protection to be a bool')
        __self__.enable_deletion_protection = enable_deletion_protection
        """
        If true, deletion of the load balancer will be disabled via
        the AWS API. This will prevent Terraform from deleting the load balancer. Defaults to `false`.
        """
        __props__['enableDeletionProtection'] = enable_deletion_protection

        if enable_http2 and not isinstance(enable_http2, bool):
            raise TypeError('Expected property enable_http2 to be a bool')
        __self__.enable_http2 = enable_http2
        """
        Indicates whether HTTP/2 is enabled in `application` load balancers. Defaults to `true`.
        """
        __props__['enableHttp2'] = enable_http2

        if idle_timeout and not isinstance(idle_timeout, int):
            raise TypeError('Expected property idle_timeout to be a int')
        __self__.idle_timeout = idle_timeout
        """
        The time in seconds that the connection is allowed to be idle. Only valid for Load Balancers of type `application`. Default: 60.
        """
        __props__['idleTimeout'] = idle_timeout

        if internal and not isinstance(internal, bool):
            raise TypeError('Expected property internal to be a bool')
        __self__.internal = internal
        """
        If true, the LB will be internal.
        """
        __props__['internal'] = internal

        if ip_address_type and not isinstance(ip_address_type, basestring):
            raise TypeError('Expected property ip_address_type to be a basestring')
        __self__.ip_address_type = ip_address_type
        """
        The type of IP addresses used by the subnets for your load balancer. The possible values are `ipv4` and `dualstack`
        """
        __props__['ipAddressType'] = ip_address_type

        if load_balancer_type and not isinstance(load_balancer_type, basestring):
            raise TypeError('Expected property load_balancer_type to be a basestring')
        __self__.load_balancer_type = load_balancer_type
        """
        The type of load balancer to create. Possible values are `application` or `network`. The default value is `application`.
        """
        __props__['loadBalancerType'] = load_balancer_type

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        The name of the LB. This name must be unique within your AWS account, can have a maximum of 32 characters,
        must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen. If not specified,
        Terraform will autogenerate a name beginning with `tf-lb`.
        """
        __props__['name'] = name

        if name_prefix and not isinstance(name_prefix, basestring):
            raise TypeError('Expected property name_prefix to be a basestring')
        __self__.name_prefix = name_prefix
        """
        Creates a unique name beginning with the specified prefix. Conflicts with `name`.
        """
        __props__['namePrefix'] = name_prefix

        if security_groups and not isinstance(security_groups, list):
            raise TypeError('Expected property security_groups to be a list')
        __self__.security_groups = security_groups
        """
        A list of security group IDs to assign to the LB. Only valid for Load Balancers of type `application`.
        """
        __props__['securityGroups'] = security_groups

        if subnet_mappings and not isinstance(subnet_mappings, list):
            raise TypeError('Expected property subnet_mappings to be a list')
        __self__.subnet_mappings = subnet_mappings
        """
        A subnet mapping block as documented below.
        """
        __props__['subnetMappings'] = subnet_mappings

        if subnets and not isinstance(subnets, list):
            raise TypeError('Expected property subnets to be a list')
        __self__.subnets = subnets
        """
        A list of subnet IDs to attach to the LB. Subnets
        cannot be updated for Load Balancers of type `network`. Changing this value
        for load balancers of type `network` will force a recreation of the resource.
        """
        __props__['subnets'] = subnets

        if tags and not isinstance(tags, dict):
            raise TypeError('Expected property tags to be a dict')
        __self__.tags = tags
        """
        A mapping of tags to assign to the resource.
        """
        __props__['tags'] = tags

        __self__.arn = pulumi.runtime.UNKNOWN
        """
        The ARN of the load balancer (matches `id`).
        """
        __self__.arn_suffix = pulumi.runtime.UNKNOWN
        """
        The ARN suffix for use with CloudWatch Metrics.
        """
        __self__.dns_name = pulumi.runtime.UNKNOWN
        """
        The DNS name of the load balancer.
        """
        __self__.vpc_id = pulumi.runtime.UNKNOWN
        __self__.zone_id = pulumi.runtime.UNKNOWN
        """
        The canonical hosted zone ID of the load balancer (to be used in a Route 53 Alias record).
        """

        super(LoadBalancer, __self__).__init__(
            'aws:applicationloadbalancing/loadBalancer:LoadBalancer',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'accessLogs' in outs:
            self.access_logs = outs['accessLogs']
        if 'arn' in outs:
            self.arn = outs['arn']
        if 'arnSuffix' in outs:
            self.arn_suffix = outs['arnSuffix']
        if 'dnsName' in outs:
            self.dns_name = outs['dnsName']
        if 'enableCrossZoneLoadBalancing' in outs:
            self.enable_cross_zone_load_balancing = outs['enableCrossZoneLoadBalancing']
        if 'enableDeletionProtection' in outs:
            self.enable_deletion_protection = outs['enableDeletionProtection']
        if 'enableHttp2' in outs:
            self.enable_http2 = outs['enableHttp2']
        if 'idleTimeout' in outs:
            self.idle_timeout = outs['idleTimeout']
        if 'internal' in outs:
            self.internal = outs['internal']
        if 'ipAddressType' in outs:
            self.ip_address_type = outs['ipAddressType']
        if 'loadBalancerType' in outs:
            self.load_balancer_type = outs['loadBalancerType']
        if 'name' in outs:
            self.name = outs['name']
        if 'namePrefix' in outs:
            self.name_prefix = outs['namePrefix']
        if 'securityGroups' in outs:
            self.security_groups = outs['securityGroups']
        if 'subnetMappings' in outs:
            self.subnet_mappings = outs['subnetMappings']
        if 'subnets' in outs:
            self.subnets = outs['subnets']
        if 'tags' in outs:
            self.tags = outs['tags']
        if 'vpcId' in outs:
            self.vpc_id = outs['vpcId']
        if 'zoneId' in outs:
            self.zone_id = outs['zoneId']
