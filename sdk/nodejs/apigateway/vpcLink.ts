// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";

/**
 * Provides an API Gateway VPC Link.
 */
export class VpcLink extends pulumi.CustomResource {
    /**
     * Get an existing VpcLink resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VpcLinkState): VpcLink {
        return new VpcLink(name, <any>state, { id });
    }

    /**
     * The description of the VPC link.
     */
    public readonly description: pulumi.Output<string | undefined>;
    /**
     * The name used to label and identify the VPC link.
     */
    public readonly name: pulumi.Output<string>;
    /**
     * The list of network load balancer arns in the VPC targeted by the VPC link. Currently AWS only supports 1 target.
     */
    public readonly targetArn: pulumi.Output<string>;

    /**
     * Create a VpcLink resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: VpcLinkArgs, opts?: pulumi.ResourceOptions)
    constructor(name: string, argsOrState?: VpcLinkArgs | VpcLinkState, opts?: pulumi.ResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: VpcLinkState = argsOrState as VpcLinkState | undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["targetArn"] = state ? state.targetArn : undefined;
        } else {
            const args = argsOrState as VpcLinkArgs | undefined;
            if (!args || args.targetArn === undefined) {
                throw new Error("Missing required property 'targetArn'");
            }
            inputs["description"] = args ? args.description : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["targetArn"] = args ? args.targetArn : undefined;
        }
        super("aws:apigateway/vpcLink:VpcLink", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering VpcLink resources.
 */
export interface VpcLinkState {
    /**
     * The description of the VPC link.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The name used to label and identify the VPC link.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The list of network load balancer arns in the VPC targeted by the VPC link. Currently AWS only supports 1 target.
     */
    readonly targetArn?: pulumi.Input<pulumi.Input<string>>;
}

/**
 * The set of arguments for constructing a VpcLink resource.
 */
export interface VpcLinkArgs {
    /**
     * The description of the VPC link.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The name used to label and identify the VPC link.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The list of network load balancer arns in the VPC targeted by the VPC link. Currently AWS only supports 1 target.
     */
    readonly targetArn: pulumi.Input<pulumi.Input<string>>;
}