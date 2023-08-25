"""An AWS Python Pulumi program"""

import pulumi
from pulumi_toolkit.ec2_instance_connect_component import EC2InstanceConnect

config = pulumi.Config()

INSTANCE_TYPE = config.require("instanceType")
AMI_ID = config.require("amiId")

print(f"Instance Type: {INSTANCE_TYPE}")
print(f"AMI ID: {AMI_ID}")

instance_connect = EC2InstanceConnect("ec2Connect-test",
                                      {
                                          'instance_type': INSTANCE_TYPE,
                                          'ami_id': AMI_ID,
                                      })

pulumi.export("instancePublicIp", instance_connect.public_ip)

