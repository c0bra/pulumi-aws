// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Use this data source to get information about an EBS volume for use in other
 * resources.
 */
export function getVolume(args?: GetVolumeArgs, opts?: pulumi.InvokeOptions): Promise<GetVolumeResult> {
    args = args || {};
    return pulumi.runtime.invoke("aws:ebs/getVolume:getVolume", {
        "filters": args.filters,
        "mostRecent": args.mostRecent,
        "tags": args.tags,
    }, opts);
}

/**
 * A collection of arguments for invoking getVolume.
 */
export interface GetVolumeArgs {
    /**
     * One or more name/value pairs to filter off of. There are
     * several valid keys, for a full reference, check out
     * [describe-volumes in the AWS CLI reference][1].
     */
    readonly filters?: { name: string, values: string[] }[];
    /**
     * If more than one result is returned, use the most
     * recent Volume.
     */
    readonly mostRecent?: boolean;
    readonly tags?: {[key: string]: any};
}

/**
 * A collection of values returned by getVolume.
 */
export interface GetVolumeResult {
    /**
     * The volume ARN (e.g. arn:aws:ec2:us-east-1:0123456789012:volume/vol-59fcb34e).
     */
    readonly arn: string;
    /**
     * The AZ where the EBS volume exists.
     */
    readonly availabilityZone: string;
    /**
     * Whether the disk is encrypted.
     */
    readonly encrypted: boolean;
    /**
     * The amount of IOPS for the disk.
     */
    readonly iops: number;
    /**
     * The ARN for the KMS encryption key.
     */
    readonly kmsKeyId: string;
    /**
     * The size of the drive in GiBs.
     */
    readonly size: number;
    /**
     * The snapshot_id the EBS volume is based off.
     */
    readonly snapshotId: string;
    /**
     * A mapping of tags for the resource.
     */
    readonly tags: {[key: string]: any};
    /**
     * The volume ID (e.g. vol-59fcb34e).
     */
    readonly volumeId: string;
    /**
     * The type of EBS volume.
     */
    readonly volumeType: string;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
