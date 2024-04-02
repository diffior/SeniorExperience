from django.db import models
import yaml

# Define your EC2Instance model with fields that represent the configuration
# of an EC2 instance as per your Ansible playbook requirements.
class EC2Instance(models.Model):
    ansible_python_interpreter = models.CharField(max_length=255, default='/usr/bin/python3')
    boto3_installed = models.BooleanField(default=True)
    botocore_installed = models.BooleanField(default=True)
    python3_version = models.CharField(max_length=50, default='Python 3.8')
    firewalld_installed = models.BooleanField(default=True)
    firewalld_started = models.BooleanField(default=True)
    http_open = models.BooleanField(default=True)
    https_open = models.BooleanField(default=True)
    application_git_repo = models.CharField(max_length=255, default='https://github.com/diffior/SeniorExperience')
    application_git_branch = models.CharField(max_length=100, default='main')
    scripts_src = models.CharField(max_length=255, default='/Users/chrii/Desktop/MSU-Denver/SeniorExp/AWS/first_playbook.yml')
    scripts_dest = models.CharField(max_length=255, default='/home/ec2-user/Scripts/scripts_EC2')

    def __str__(self):
        return f"EC2 Instance Config for {self.id}"

    # Method to generate an Ansible playbook in YAML format based on the instance's data.
    def to_ansible_playbook(self):
        playbook = [
            {
                'name': 'Setup and Manage AWS EC2 Instance',
                'hosts': 'localhost',
                'gather_facts': False,
                'vars': {
                    'ansible_python_interpreter': self.ansible_python_interpreter,
                },
                'tasks': [
                    {
                        'name': 'Ensure boto3 and botocore are installed',
                        'ansible.builtin.pip': {
                            'name': ['boto3', 'botocore'],
                            'state': 'present',
                        },
                    },
                ],
            },
            {
                'name': 'Ensure Python is installed on EC2 Instance and configure firewall',
                'hosts': 'ec2_instance',
                'become': True,
                'tasks': [
                    {
                        'name': 'Check if Python3 is present',
                        'command': 'python3 --version',
                        'ignore_errors': True,
                        'register': 'python3_check',
                        'changed_when': False,
                        'failed_when': False,
                    },
                    {
                        'name': 'Ensure Python3 is installed',
                        'ansible.builtin.yum': {
                            'name': 'python3',
                            'state': 'present',
                        },
                        'when': 'python3_check is failed',
                    },
                    {
                        'name': 'Update all packages on a Red Hat-based system',
                        'ansible.builtin.yum': {
                            'name': '*',
                            'state': 'latest',
                        },
                        'when': 'all_packages_updated',
                    },
                    {
                        'name': 'Ensure firewalld is installed',
                        'ansible.builtin.yum': {
                            'name': 'firewalld',
                            'state': 'present',
                        },
                        'when': 'firewalld_installed',
                    },
                    {
                        'name': 'Start and enable firewalld',
                        'ansible.builtin.service': {
                            'name': 'firewalld',
                            'state': 'started',
                            'enabled': True,
                        },
                        'when': 'firewalld_started',
                    },
                    {
                        'name': 'Open HTTP port on firewalld',
                        'ansible.builtin.firewalld': {
                            'service': 'http',
                            'state': 'enabled',
                            'permanent': True,
                            'immediate': True,
                        },
                        'when': 'http_open',
                    },
                    {
                        'name': 'Open HTTPS port on firewalld',
                        'ansible.builtin.firewalld': {
                            'service': 'https',
                            'state': 'enabled',
                            'permanent': True,
                            'immediate': True,
                        },
                        'when': 'https_open',
                    },
                    {
                        'name': 'Deploy application from Git repository',
                        'ansible.builtin.git': {
                            'repo': self.application_git_repo,
                            'dest': '/var/www/html/myapp',
                            'version': self.application_git_branch,
                        },
                    },
                    {
                        'name': 'Copy files to instance',
                        'ansible.builtin.copy': {
                            'src': self.scripts_src,
                            'dest': self.scripts_dest,
                        },
                    },
                ],
            },
        ]

        # If you want to start the playbook with '---', you can prepend it here.
        # This is optional and usually not required unless your YAML parser requires it.
        playbook_yaml = '---\n' + yaml.dump(playbook, sort_keys=False, default_flow_style=False)
        return playbook_yaml
