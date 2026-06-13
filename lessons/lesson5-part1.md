# Install Nimbus Web App inside a VPC

## Make Nimbus into a Streamlit web app - using AI

In this step, you will convert the code inside the `notebooks/` folder into a simple web app using **Streamlit**.

Streamlit lets you create a web UI directly in Python.

---

### Step 1: Create an app folder

From the root of your repo:

```bash
cd smu-cce
mkdir app
```

---

### Step 2: Ask AI to convert the notebooks into a Streamlit app

Use this prompt in Copilot / Codex / ChatGPT:

```text
I have a repo with Python code inside the notebooks/ folder.

Create a simple Streamlit web app using the code in notebooks/.

Goal:
Convert the notebook logic into a beginner-friendly Streamlit application.

Requirements:
- Read the notebooks inside the notebooks/ folder
- Extract reusable Python functions from the notebooks
- Create a Streamlit app inside a new app/ folder
- Main file should be app/app.py
- The UI should have:
  - Text input for ticker symbol
  - Dropdown to choose analysis type:
    - filings
    - news
    - stock price ratings
  - A button called Run
- When the user clicks Run, call the correct function based on the selected analysis
- Display results clearly using Streamlit components such as:
  - st.write()
  - st.dataframe()
  - st.metric()
- Add basic error handling
- Create or update requirements.txt with required packages
- Keep the code simple and suitable for students

Expected output:
- app/app.py
- Any helper Python files needed
- Updated requirements.txt
- Short explanation of how to run the app
```

---

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

If Streamlit is not already included:

```bash
pip install streamlit
```

---

### Step 4: Run the Streamlit app

```bash
python3 -m streamlit run app/app.py
```

---

### Step 5: Open the app

In Codespaces, open the forwarded port shown by Streamlit.

Usually Streamlit runs on:

```text
http://localhost:8501
```

---

## Install and run the Nimbus web app in the Sandbox environment (identical set-up to Lab 2)

### Activate the Sandbox Environment 

- On your Course Dashboard, go to Modules. Scroll down to `Sandbox`. Click `Sandbox Environment`
- Click `Start Lab`. Wait for completion (this may take several minutes)
- Once completed. Click `AWS`

### Create the VPC set-up 
Download the file `scripts/lesson5-vpc-cf.yml` to your laptop. This is an AWS CloudFormation script.

AWS CloudFormation (CF) is an Infrastructure as Code (IaC) service that allows you to define AWS resources in a text file and deploy them automatically. Instead of creating resources manually in the AWS Console, CloudFormation creates and configures them for you.

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

### Start an EC2 instance 

This is your web server. 

**EC2 set-up**

```text
Amazon Linux (default)
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
yum update -y

# Install software
yum install -y git python3 python3-pip
```

Click Launch Instance (Choose Proceed Without Key Pair)

### Start Streamlit App 

- Wait for `web-server` Instance to be Ready (All checks passed). This may take several minutes
- Choose the `web-server` instance. Click `Connect`
- Under tab `SSM Session Manager` click `Connect`

You will see the linux prompt. 

- Clone the git repo and run the app  

```bash 
# Clone repo
git clone https://github.com/2gauravc/smu-cce.git

# Install Python dependencies
cd smu-cce
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

# Start Streamlit App
python3 -m streamlit run app/app.py 
```

### Access the app 

Copy the Public IPv4 DNS of the EC2 server shown in the Details tab. 

go to a web browser, paste the `Public IPv4 DNS`:8501 to access the app. 