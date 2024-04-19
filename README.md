# Ansible GUI. Project Big A

## Introduction
Big A is a Senior Experience project developed by Christian Campbell, Joshua Lee, Myles Bunde Green, Grady Rowedder, Sam Schultz, and Kyle Hossman. This project provides a user-friendly GUI for generating Ansible playbooks.

## What is Anisbile 
- Open-source tool: Ansible is freely available and used for automating IT tasks like software deployment, configuration management, and more.

- Simple and Fast: Designed for ease of use, it's accessible to professionals without extensive programming skills.

- Agentless technology: Does not require installing any additional software on the nodes (servers, clients, devices) it manages

- Uses SSH for connections: Connects to nodes using SSH (Secure Shell), a secure network protocol, to execute tasks.

- Modules-driven: Utilizes small programs called modules to manage and bring systems to their desired state; these modules are removed after execution.

- Security and reliability: Emphasizes security with support for various authentication mechanisms, including SSH keys.

- Wide compatibility: Works across different systems, supporting both Unix-like platforms and Microsoft environments.

- Scalable architecture: Designed to handle complex IT environments effectively, ensuring consistent and scalable operations.

## Features
- GUI that will generate a functioning playbook written in YAML.
- Given a basic template of an EC2 playbook.
- Generates a personal inventory file for users and hostfiles.
- Ability to run on Nginx and Gunicorn, enhancing server persistence, scalability, and elasticity.
- Hosted on diffior.pythonanywhere.com (Expires July-19-2024)

## Prerequisites
- Python 3.12.3 or newer 
- All dependencies are listed within the requirements.txt file.

## Installation

1. Clone the repository: git clone https://github.com/diffior/SeniorExperience.git
2. cd SeniorExperience/big_a
3. Create or use myprojectenv
4. source myprojectenv/bin/activate
5. pip install requirements.txt

## Run applicaiton
1. python manage.py makemigration
2. python manage.py migrate
3. python manage.py runserver 3000
