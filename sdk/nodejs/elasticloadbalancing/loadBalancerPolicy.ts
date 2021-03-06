// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Provides a load balancer policy, which can be attached to an ELB listener or backend server.
 */
export class LoadBalancerPolicy extends pulumi.CustomResource {
    /**
     * Get an existing LoadBalancerPolicy resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: LoadBalancerPolicyState): LoadBalancerPolicy {
        return new LoadBalancerPolicy(name, <any>state, { id });
    }

    /**
     * The load balancer on which the policy is defined.
     */
    public readonly loadBalancerName: pulumi.Output<string>;
    /**
     * Policy attribute to apply to the policy.
     */
    public readonly policyAttributes: pulumi.Output<{ name?: string, value?: string }[] | undefined>;
    /**
     * The name of the load balancer policy.
     */
    public readonly policyName: pulumi.Output<string>;
    /**
     * The policy type.
     */
    public readonly policyTypeName: pulumi.Output<string>;

    /**
     * Create a LoadBalancerPolicy resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: LoadBalancerPolicyArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: LoadBalancerPolicyArgs | LoadBalancerPolicyState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: LoadBalancerPolicyState = argsOrState as LoadBalancerPolicyState | undefined;
            inputs["loadBalancerName"] = state ? state.loadBalancerName : undefined;
            inputs["policyAttributes"] = state ? state.policyAttributes : undefined;
            inputs["policyName"] = state ? state.policyName : undefined;
            inputs["policyTypeName"] = state ? state.policyTypeName : undefined;
        } else {
            const args = argsOrState as LoadBalancerPolicyArgs | undefined;
            if (!args || args.loadBalancerName === undefined) {
                throw new Error("Missing required property 'loadBalancerName'");
            }
            if (!args || args.policyName === undefined) {
                throw new Error("Missing required property 'policyName'");
            }
            if (!args || args.policyTypeName === undefined) {
                throw new Error("Missing required property 'policyTypeName'");
            }
            inputs["loadBalancerName"] = args ? args.loadBalancerName : undefined;
            inputs["policyAttributes"] = args ? args.policyAttributes : undefined;
            inputs["policyName"] = args ? args.policyName : undefined;
            inputs["policyTypeName"] = args ? args.policyTypeName : undefined;
        }
        super("aws:elasticloadbalancing/loadBalancerPolicy:LoadBalancerPolicy", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering LoadBalancerPolicy resources.
 */
export interface LoadBalancerPolicyState {
    /**
     * The load balancer on which the policy is defined.
     */
    readonly loadBalancerName?: pulumi.Input<string>;
    /**
     * Policy attribute to apply to the policy.
     */
    readonly policyAttributes?: pulumi.Input<pulumi.Input<{ name?: pulumi.Input<string>, value?: pulumi.Input<string> }>[]>;
    /**
     * The name of the load balancer policy.
     */
    readonly policyName?: pulumi.Input<string>;
    /**
     * The policy type.
     */
    readonly policyTypeName?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a LoadBalancerPolicy resource.
 */
export interface LoadBalancerPolicyArgs {
    /**
     * The load balancer on which the policy is defined.
     */
    readonly loadBalancerName: pulumi.Input<string>;
    /**
     * Policy attribute to apply to the policy.
     */
    readonly policyAttributes?: pulumi.Input<pulumi.Input<{ name?: pulumi.Input<string>, value?: pulumi.Input<string> }>[]>;
    /**
     * The name of the load balancer policy.
     */
    readonly policyName: pulumi.Input<string>;
    /**
     * The policy type.
     */
    readonly policyTypeName: pulumi.Input<string>;
}
