# Use AI to generate IaC script 

Extend IaC script from lesson 5 (VPC set-up) to incldue EC2 set-up and app install and run. 

## Step 1 - Set-up code repo 

Copy `lesson5-vpc-cf.yml` to a new yml file. 

```bash 
cp scripts/lesson5-vpc-cf.yml scripts/lesson6-new.yml 
```

## Step 2 - Describe what you want 

Use this prompt:

Generate a new Cloud Formation script. Use the existing Cloud Formation script under `scripts/lesson6-new.yml` and add the folliwng to it.

1. EC2 set-up

Amazon Linux (latest 2023 AMIID: ami-08f44e8eca9095668)
t2.micro 
Key pair: leave blank 
Network: Edit. Choose `lab-vpc` 
Subnet: lab-subnet-public2 (not Private!)
Auto-assign public IP: Enable
Security Group - `Web Security Group`
Advanced Details -> IAM Profile: `LabInstanceProfile` (IMPORTANT)

Advanced Details -> User data

#!/bin/bash
dnf update -y
dnf install -y git python3-pip

cd /home/ec2-user
git clone https://github.com/2gauravc/smu-cce.git
python3 -m venv venv
source venv/bin/activate
          
cd smu-cce

python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

nohup python3 -m streamlit run app/app.py \
    --server.port 8501 \
    --server.address 0.0.0.0 \
    > /home/ec2-user/streamlit.log 2>&1 &

2. Change the Output 

Change the Output of the script to show the Pubic IPv4 address of the EC2 instance 


## Step 3 Run & Verify 

- Copy the Public IPv4 DNS of the EC2 server shown in the Details tab. 
- Go to a web browser, paste the `Public IPv4 DNS`:8501 to access the app. 
