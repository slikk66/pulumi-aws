# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class UserProfile(pulumi.CustomResource):
    """
    Provides an OpsWorks User Profile resource.
    """
    def __init__(__self__, __name__, __opts__=None, allow_self_management=None, ssh_public_key=None, ssh_username=None, user_arn=None):
        """Create a UserProfile resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if allow_self_management and not isinstance(allow_self_management, bool):
            raise TypeError('Expected property allow_self_management to be a bool')
        __self__.allow_self_management = allow_self_management
        """
        Whether users can specify their own SSH public key through the My Settings page
        """
        __props__['allowSelfManagement'] = allow_self_management

        if ssh_public_key and not isinstance(ssh_public_key, basestring):
            raise TypeError('Expected property ssh_public_key to be a basestring')
        __self__.ssh_public_key = ssh_public_key
        """
        The users public key
        """
        __props__['sshPublicKey'] = ssh_public_key

        if not ssh_username:
            raise TypeError('Missing required property ssh_username')
        elif not isinstance(ssh_username, basestring):
            raise TypeError('Expected property ssh_username to be a basestring')
        __self__.ssh_username = ssh_username
        """
        The ssh username, with witch this user wants to log in
        """
        __props__['sshUsername'] = ssh_username

        if not user_arn:
            raise TypeError('Missing required property user_arn')
        elif not isinstance(user_arn, basestring):
            raise TypeError('Expected property user_arn to be a basestring')
        __self__.user_arn = user_arn
        """
        The user's IAM ARN
        """
        __props__['userArn'] = user_arn

        super(UserProfile, __self__).__init__(
            'aws:opsworks/userProfile:UserProfile',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'allowSelfManagement' in outs:
            self.allow_self_management = outs['allowSelfManagement']
        if 'sshPublicKey' in outs:
            self.ssh_public_key = outs['sshPublicKey']
        if 'sshUsername' in outs:
            self.ssh_username = outs['sshUsername']
        if 'userArn' in outs:
            self.user_arn = outs['userArn']
