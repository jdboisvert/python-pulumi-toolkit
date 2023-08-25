# Features of the library

## Components (Classes)
### EC2InstanceConnect
This is used to connect to an EC2 instance using EC2 Instance Connect. This will set up a EC2 server that can only be access via [EC2 Connect](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-connect-set-up.html) and now allow SSH access. This is useful for when you want to allow SSH access to an EC2 instance but don't want to expose SSH to the internet.

Note currently this only works with Ubuntu AMIs. 

Once this is created there will be a Group created in IAM called `EC2InstanceConnect` that will have the necessary permissions to connect to the EC2 instance. This is what you will attach to IAM users or roles to allow them to connect to the EC2 instance.

#### Example
In the `__main__.py` file:
```python
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
```

The corresponding `Pulumi.<stack name>.yaml` file:
```yaml
config:
  aws:region: us-east-1  # Used to set the region for the EC2 instance change this as needed.
  pulumi-playground:instanceType: t2.micro
  pulumi-playground:amiId: ami-0ea18256de20ecdfc  # This works with Ubtunu currently ensure that the AMI ID is correct for the region and is Ubuntu
```

