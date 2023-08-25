import pulumi
from pulumi import ComponentResource
from pulumi_aws import ec2, iam

class EC2InstanceConnect(ComponentResource):
    def __init__(self, name: str, args: dict, opts: pulumi.ResourceOptions = None):
        super().__init__('custom:resource:EC2InstanceConnect', name, {}, opts)

        instance_type = args.get('instance_type')
        ami_id = args.get('ami_id')

        sg = ec2.SecurityGroup(
            f"{name}-sg",
            description="Allow SSH inbound traffic",
            ingress=[
                {
                    "protocol": "tcp",
                    "from_port": 22,
                    "to_port": 22,
                    "cidr_blocks": ["0.0.0.0/0"]
                }
            ],
            opts=pulumi.ResourceOptions(parent=self)
        )

        # Updated user data for Ubuntu
        user_data_script = """#!/bin/bash
        sudo apt-get update
        sudo apt-get install -y ec2-instance-connect
        echo 'AuthorizedKeysCommand /usr/share/ec2-instance-connect/eic_run_authorized_keys %%u %%f' >> /etc/ssh/sshd_config
        echo 'AuthorizedKeysCommandUser ec2-instance-connect' >> /etc/ssh/sshd_config
        service sshd restart
        """

        ec2_instance = ec2.Instance(
            f"{name}-instance",
            instance_type=instance_type,
            ami=ami_id,
            vpc_security_group_ids=[sg.id],
            user_data=user_data_script,
            tags={
                "Name": f"{name}-instance"
            },
            opts=pulumi.ResourceOptions(parent=self)
        )

        user_group = iam.Group(
            f"{name}-EC2ConnectUsers",
            opts=pulumi.ResourceOptions(parent=self)
        )

        ec2_connect_policy = iam.Policy(
            f"{name}-policy",
            description="Policy to allow EC2 Instance Connect",
            policy=ec2_instance.arn.apply(lambda arn: f'{{"Version": "2012-10-17","Statement": [{{"Effect": "Allow","Action": "ec2-instance-connect:SendSSHPublicKey","Resource": "{arn}"}}]}}'),
            opts=pulumi.ResourceOptions(parent=self)
        )

        iam.GroupPolicyAttachment(
            f"{name}-policy-attachment",
            policy_arn=ec2_connect_policy.arn,
            group=user_group.name,
            opts=pulumi.ResourceOptions(parent=self)
        )

        self.public_ip = ec2_instance.public_ip
        self.register_outputs({"public_ip": self.public_ip})
