// *** WARNING: this file was generated by the Pulumi Terraform Bridge (TFGEN) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "pulumi";

export function getListenerInfo(args: GetListenerInfoArgs): Promise<GetListenerInfoResult> {
    return pulumi.runtime.invoke("aws:applicationloadbalancing/getListenerInfo:getListenerInfo", {
        "arn": args.arn,
    });
}

/**
 * A collection of arguments for invoking getListenerInfo.
 */
export interface GetListenerInfoArgs {
    arn: pulumi.ComputedValue<string>;
}

/**
 * A collection of values returned by getListenerInfo.
 */
export interface GetListenerInfoResult {
    certificateArn: string;
    defaultAction: { targetGroupArn: string, type: string }[];
    loadBalancerArn: string;
    port: number;
    protocol: string;
    sslPolicy: string;
}
