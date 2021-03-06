# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class Budget(pulumi.CustomResource):
    """
    Provides a budgets budget resource. Budgets use the cost visualisation provided by Cost Explorer to show you the status of your budgets, to provide forecasts of your estimated costs, and to track your AWS usage, including your free tier usage.
    """
    def __init__(__self__, __name__, __opts__=None, account_id=None, budget_type=None, cost_filters=None, cost_types=None, limit_amount=None, limit_unit=None, name=None, name_prefix=None, time_period_end=None, time_period_start=None, time_unit=None):
        """Create a Budget resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if account_id and not isinstance(account_id, basestring):
            raise TypeError('Expected property account_id to be a basestring')
        __self__.account_id = account_id
        """
        The ID of the target account for budget. Will use current user's account_id by default if omitted.
        """
        __props__['accountId'] = account_id

        if not budget_type:
            raise TypeError('Missing required property budget_type')
        elif not isinstance(budget_type, basestring):
            raise TypeError('Expected property budget_type to be a basestring')
        __self__.budget_type = budget_type
        """
        Whether this budget tracks monetary cost or usage.
        """
        __props__['budgetType'] = budget_type

        if cost_filters and not isinstance(cost_filters, dict):
            raise TypeError('Expected property cost_filters to be a dict')
        __self__.cost_filters = cost_filters
        """
        Map of CostFilters key/value pairs to apply to the budget.
        """
        __props__['costFilters'] = cost_filters

        if cost_types and not isinstance(cost_types, dict):
            raise TypeError('Expected property cost_types to be a dict')
        __self__.cost_types = cost_types
        """
        Object containing CostTypes The types of cost included in a budget, such as tax and subscriptions..
        """
        __props__['costTypes'] = cost_types

        if not limit_amount:
            raise TypeError('Missing required property limit_amount')
        elif not isinstance(limit_amount, basestring):
            raise TypeError('Expected property limit_amount to be a basestring')
        __self__.limit_amount = limit_amount
        """
        The amount of cost or usage being measured for a budget.
        """
        __props__['limitAmount'] = limit_amount

        if not limit_unit:
            raise TypeError('Missing required property limit_unit')
        elif not isinstance(limit_unit, basestring):
            raise TypeError('Expected property limit_unit to be a basestring')
        __self__.limit_unit = limit_unit
        """
        The unit of measurement used for the budget forecast, actual spend, or budget threshold, such as dollars or GB. See [Spend ](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/data-type-spend.html) documentation.
        """
        __props__['limitUnit'] = limit_unit

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        The name of a budget. Unique within accounts.
        """
        __props__['name'] = name

        if name_prefix and not isinstance(name_prefix, basestring):
            raise TypeError('Expected property name_prefix to be a basestring')
        __self__.name_prefix = name_prefix
        """
        The prefix of the name of a budget. Unique within accounts.
        """
        __props__['namePrefix'] = name_prefix

        if time_period_end and not isinstance(time_period_end, basestring):
            raise TypeError('Expected property time_period_end to be a basestring')
        __self__.time_period_end = time_period_end
        """
        The end of the time period covered by the budget. There are no restrictions on the end date. Format: `2017-01-01_12:00`.
        """
        __props__['timePeriodEnd'] = time_period_end

        if not time_period_start:
            raise TypeError('Missing required property time_period_start')
        elif not isinstance(time_period_start, basestring):
            raise TypeError('Expected property time_period_start to be a basestring')
        __self__.time_period_start = time_period_start
        """
        The start of the time period covered by the budget. The start date must come before the end date. Format: `2017-01-01_12:00`.
        """
        __props__['timePeriodStart'] = time_period_start

        if not time_unit:
            raise TypeError('Missing required property time_unit')
        elif not isinstance(time_unit, basestring):
            raise TypeError('Expected property time_unit to be a basestring')
        __self__.time_unit = time_unit
        """
        The length of time until a budget resets the actual and forecasted spend. Valid values: `MONTHLY`, `QUARTERLY`, `ANNUALLY`.
        """
        __props__['timeUnit'] = time_unit

        super(Budget, __self__).__init__(
            'aws:budgets/budget:Budget',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'accountId' in outs:
            self.account_id = outs['accountId']
        if 'budgetType' in outs:
            self.budget_type = outs['budgetType']
        if 'costFilters' in outs:
            self.cost_filters = outs['costFilters']
        if 'costTypes' in outs:
            self.cost_types = outs['costTypes']
        if 'limitAmount' in outs:
            self.limit_amount = outs['limitAmount']
        if 'limitUnit' in outs:
            self.limit_unit = outs['limitUnit']
        if 'name' in outs:
            self.name = outs['name']
        if 'namePrefix' in outs:
            self.name_prefix = outs['namePrefix']
        if 'timePeriodEnd' in outs:
            self.time_period_end = outs['timePeriodEnd']
        if 'timePeriodStart' in outs:
            self.time_period_start = outs['timePeriodStart']
        if 'timeUnit' in outs:
            self.time_unit = outs['timeUnit']
