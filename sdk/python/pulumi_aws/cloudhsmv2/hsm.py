# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class Hsm(pulumi.CustomResource):
    """
    Creates an HSM module in Amazon CloudHSM v2 cluster.
    """
    def __init__(__self__, __name__, __opts__=None, availability_zone=None, cluster_id=None, ip_address=None, subnet_id=None):
        """Create a Hsm resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if availability_zone and not isinstance(availability_zone, basestring):
            raise TypeError('Expected property availability_zone to be a basestring')
        __self__.availability_zone = availability_zone
        """
        The IDs of AZ in which HSM module will be located. Do not use together with subnet_id.
        """
        __props__['availabilityZone'] = availability_zone

        if not cluster_id:
            raise TypeError('Missing required property cluster_id')
        elif not isinstance(cluster_id, basestring):
            raise TypeError('Expected property cluster_id to be a basestring')
        __self__.cluster_id = cluster_id
        """
        The ID of Cloud HSM v2 cluster to which HSM will be added.
        """
        __props__['clusterId'] = cluster_id

        if ip_address and not isinstance(ip_address, basestring):
            raise TypeError('Expected property ip_address to be a basestring')
        __self__.ip_address = ip_address
        """
        The IP address of HSM module. Must be within the CIDR of selected subnet.
        """
        __props__['ipAddress'] = ip_address

        if subnet_id and not isinstance(subnet_id, basestring):
            raise TypeError('Expected property subnet_id to be a basestring')
        __self__.subnet_id = subnet_id
        """
        The ID of subnet in which HSM module will be located.
        """
        __props__['subnetId'] = subnet_id

        __self__.hsm_eni_id = pulumi.runtime.UNKNOWN
        """
        The id of the ENI interface allocated for HSM module.
        """
        __self__.hsm_id = pulumi.runtime.UNKNOWN
        """
        The id of the HSM module.
        """
        __self__.hsm_state = pulumi.runtime.UNKNOWN
        """
        The state of the HSM module.
        """

        super(Hsm, __self__).__init__(
            'aws:cloudhsmv2/hsm:Hsm',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'availabilityZone' in outs:
            self.availability_zone = outs['availabilityZone']
        if 'clusterId' in outs:
            self.cluster_id = outs['clusterId']
        if 'hsmEniId' in outs:
            self.hsm_eni_id = outs['hsmEniId']
        if 'hsmId' in outs:
            self.hsm_id = outs['hsmId']
        if 'hsmState' in outs:
            self.hsm_state = outs['hsmState']
        if 'ipAddress' in outs:
            self.ip_address = outs['ipAddress']
        if 'subnetId' in outs:
            self.subnet_id = outs['subnetId']
