# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class MountTarget(pulumi.CustomResource):
    """
    Provides an Elastic File System (EFS) mount target.
    """
    def __init__(__self__, __name__, __opts__=None, file_system_id=None, ip_address=None, security_groups=None, subnet_id=None):
        """Create a MountTarget resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not file_system_id:
            raise TypeError('Missing required property file_system_id')
        elif not isinstance(file_system_id, basestring):
            raise TypeError('Expected property file_system_id to be a basestring')
        __self__.file_system_id = file_system_id
        """
        The ID of the file system for which the mount target is intended.
        """
        __props__['fileSystemId'] = file_system_id

        if ip_address and not isinstance(ip_address, basestring):
            raise TypeError('Expected property ip_address to be a basestring')
        __self__.ip_address = ip_address
        """
        The address (within the address range of the specified subnet) at
        which the file system may be mounted via the mount target.
        """
        __props__['ipAddress'] = ip_address

        if security_groups and not isinstance(security_groups, list):
            raise TypeError('Expected property security_groups to be a list')
        __self__.security_groups = security_groups
        """
        A list of up to 5 VPC security group IDs (that must
        be for the same VPC as subnet specified) in effect for the mount target.
        """
        __props__['securityGroups'] = security_groups

        if not subnet_id:
            raise TypeError('Missing required property subnet_id')
        elif not isinstance(subnet_id, basestring):
            raise TypeError('Expected property subnet_id to be a basestring')
        __self__.subnet_id = subnet_id
        """
        The ID of the subnet to add the mount target in.
        """
        __props__['subnetId'] = subnet_id

        __self__.dns_name = pulumi.runtime.UNKNOWN
        """
        The DNS name for the given subnet/AZ per [documented convention](http://docs.aws.amazon.com/efs/latest/ug/mounting-fs-mount-cmd-dns-name.html).
        """
        __self__.network_interface_id = pulumi.runtime.UNKNOWN
        """
        The ID of the network interface that Amazon EFS created when it created the mount target.
        """

        super(MountTarget, __self__).__init__(
            'aws:efs/mountTarget:MountTarget',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'dnsName' in outs:
            self.dns_name = outs['dnsName']
        if 'fileSystemId' in outs:
            self.file_system_id = outs['fileSystemId']
        if 'ipAddress' in outs:
            self.ip_address = outs['ipAddress']
        if 'networkInterfaceId' in outs:
            self.network_interface_id = outs['networkInterfaceId']
        if 'securityGroups' in outs:
            self.security_groups = outs['securityGroups']
        if 'subnetId' in outs:
            self.subnet_id = outs['subnetId']
