
# Use AI to generate IaC script. Install and run Nimbus app on EC2

## Task 1: Generate IaC script to create VPC set-up. 

Use AI to generate an IaC script. IaC script should create the VPC set-up (same as Lab 2) 

### Step 1: Create a `scripts` folder 

From the root of your repo:

```bash
cd smu-cce
mkdir scripts/
```


### Step 2: Describe what you want 

```text
Use this prompt:

Create an AWS CloudFormation YAML IaC template for us-east-1. Save the template to scripts/lesson5-vpc-cf.yml

The template should build the following VPC lab environment:

1. VPC
- Name: LabVPC
- CIDR: 10.0.0.0/16
- Enable DNS hostnames
- Enable DNS resolution

2. Internet Gateway
- Name: lab-igw
- Attach it to lab-vpc

3. Public subnets
Create two public subnets:
- lab-subnet-public1-us-east-1a
  - AZ: us-east-1a
  - CIDR: 10.0.0.0/24
  - Auto-assign public IPv4 enabled

- lab-subnet-public2
  - AZ: us-east-1b
  - CIDR: 10.0.2.0/24
  - Auto-assign public IPv4 enabled

4. Private subnets
Create two private subnets:
- lab-subnet-private1-us-east-1a
  - AZ: us-east-1a
  - CIDR: 10.0.1.0/24

- lab-subnet-private2
  - AZ: us-east-1b
  - CIDR: 10.0.3.0/24

5. NAT Gateway
- Create one NAT Gateway in lab-subnet-public1-us-east-1a
- Create and attach an Elastic IP for the NAT Gateway
- Name: lab-nat-public1-us-east-1a

6. Route tables
Create a public route table:
- Name: lab-rtb-public
- Route 0.0.0.0/0 to the Internet Gateway
- Associate it with both public subnets

Create a private route table:
- Name: lab-rtb-private1-us-east-1a
- Route 0.0.0.0/0 to the NAT Gateway
- Associate it with both private subnets

7. Security Group
Create a security group:
- Name: Web Security Group
- Description: Enable HTTP access
- VPC: lab-vpc
- Inbound rule:
  - Type: HTTP
  - Protocol: TCP
  - Port: 80 and 8501 
  - Source: 0.0.0.0/0
  - Description: Permit web requests (and Streamlit)

8. Outputs
Include outputs for:
- VPC ID
- Public subnet IDs
- Private subnet IDs
- Internet Gateway ID
- NAT Gateway ID
- Public route table ID
- Private route table ID
- Security group ID

Requirements:
- Use valid CloudFormation YAML.
- Use clear logical resource names.
- Add Name tags to all resources.
- Add comments explaining each major section.
- Do not include EC2 instances.
- Make the template suitable for students learning AWS networking.
```

### Step3: Run and verify 

Run the IaC script on the Sandbox environment. 

#### Activate the Sandbox Environment 

- On your Course Dashboard, go to Modules. Scroll down to `Sandbox`. Click `Sandbox Environment`
- Click `Start Lab`. Wait for completion (this may take several minutes)
- Click `AWS`

#### Run the IaC script as create the set-up

Download the IaC file generated from `scripts/lesson5-vpc-cf.yml` to your laptop. This is an AWS CloudFormation script.

We will use Cloud Formation service to set-up the infrastructure using this script. 

1. Got to the AWS Management Console of the Sandbox environment
2. In the search bar, search for **CloudFormation** and open the service.
3. Click **Create stack** and select **With new resources (standard)**.
4. Under **Specify template**, select **Upload a template file**.
5. Click **Choose file** and select the downloaded file:
   `lesson5-vpc-cf.yml`
6. Click **Next**.
7. Enter a stack name:
   `lesson5-vpc`
8. Leave the default settings unchanged unless instructed otherwise.
9. Click **Next**.
10. Review the stack configuration.
11. Scroll to the bottom of the page and click **Submit**.
12. Wait for the stack status to change from **CREATE_IN_PROGRESS** to **CREATE_COMPLETE**. This may take several minutes
13. Once the stack has been created successfully, open the **Resources** tab to view information about the resources that were created. Note that `LabVPC` was created 


## Task 2 - Start an EC2 instance 

The IaC template has set-up the VPC and the security group. Now we create the EC2 instance. This is your web server. 

**EC2 set-up**

```text
Amazon Linux 2023 (default. Notice the AMI ID 
t2.micro 
Key pair: leave blank 
Network: Edit. Choose `lab-vpc` 
Subnet: lab-subnet-public2 (not Private!)
Auto-assign public IP: Enable
Security Group - `Web Security Group`
Advanced Details -> IAM Profile: `LabInstanceProfile` (IMPORTANT)
```

Advanced Details -> User data. Copy and paste the code shown below

```bash 
#!/bin/bash
# Update packages
dnf update -y
# Install software
dnf install -y git python3 python3-pip
```

Click Launch Instance (Choose Proceed Without Key Pair)

## Task 3 - Install and run Nimbus App 

### Start Streamlit App 

- Wait for `web-server` Instance to be Ready (All checks passed). This may take several minutes
- Choose the `web-server` instance. Click `Connect`
- Under tab `SSM Session Manager` click `Connect`

You will see the linux prompt. 

- Clone the git repo and run the app  

```bash 
# Clone repo
cd ~ #go to user home directory
git clone https://github.com/2gauravc/smu-cce.git

# Create Environment 
python3 -m venv venv
source venv/bin/activate

cd smu-cce/ 

# Install Python dependencies
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

# Start Streamlit App
python3 -m streamlit run app/app.py 
```

### Access the app 

- Copy the Public IPv4 DNS of the EC2 server shown in the Details tab. 
- Go to a web browser, paste the `Public IPv4 DNS`:8501 to access the app. 

