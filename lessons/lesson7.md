# Use AI to generate app feature code & IaC script

Make two changes to the app: 

1) Implement the storage layer (new EBS volume) - IaC script 
2) Implement the UI changes to show the saved analyses 

## Task 1: Use AI to generate IaC script 

Extend the Cloud Formation IaC script to add a new EBS volume and mount it on EC2 

### Step 1: Set-up the code repo 

Copy `lesson6-vpc-ec2-app-cf.yml` to a new yml file. Call it `lesson7-vpc-ec2-app-ebs-cf.yml`

### Step 2: Describe what you want 

Use this prompt:

```text
Modify the existing IaC script (scripts/lesson7-vpc-ec2-app-ebs-cf.yml) to:

- Create additional EBS volume 
- Mount the volume as /analyses-data using user data on the EC2 instance 

Do not make any other changes to the script. 

Requirements:
- Use valid CloudFormation YAML.
- Use clear logical resource names.
- Add Name tags to all resources.
- Add comments explaining each major section.
- Make the template suitable for students learning AWS networking.

```

### Step 3: Run and verify 

Verify that: 

1. The app runs 

On the browser go to 
<ec2instance public ip>:8501 

2. The EBS volume is mounted 

Login to the EC2 instance via Connect -> SSM Session Manager. 
On the linux terminal 

```bash 
df -h 
```
You should see something like: 

sh-5.2$ df -h
Filesystem      Size  Used Avail Use% Mounted on
devtmpfs        464M     0  464M   0% /dev
tmpfs           479M     0  479M   0% /dev/shm
tmpfs           192M  412K  192M   1% /run
/dev/xvda1      8.0G  2.3G  5.7G  29% /
tmpfs           479M     0  479M   0% /tmp
/dev/xvda128     10M  1.3M  8.7M  13% /boot/efi
/dev/xvdf       9.8G   24K  9.3G   1% /analyses-data

## Task 2: Use AI to generate app feature code 

Modify the existing app code (under app/) to:

1. Convert analysis to md file (text)
2. Save it on EBS (intuitive names)
3. Show list of prev analyses on UI (read from storage) 
4. User can view prev analysis by clicking on UI  

### Step 1: Set-up the code repo 

Plan the changes. 

1. When user chooses to save the analysis (via a button on the homepage - when an analysis is displaying)
    a) New helper function to save existing analysis as md 
    b) New helper function to come up with an intuitive filename based on the ticker and otehr paramter selections 
    b) New helper function write the md file to disk -> /analyses-data
2. New section on the homepage screen to show all files in /analyses-data as links 
3. When users clicks on one link, the md file is shown on a new tab  

### Step 2: Describe what you want 

Use the following prompt:

```text
Add a new feature to the app to save and retrieve previous analysis. The changes go into the files in app/ folder. 

This is the new feature definition. 

1. When user chooses to save the analysis (via a button on the homepage - when an analysis is displaying)
    a) New helper function to save existing analysis as md 
    b) New helper function to come up with an intuitive filename based on the ticker and other paramter selections 
    b) New helper function write the md file to disk -> /analyses-data
2. New section on the homepage screen to show all files in /analyses-data as links 
3. When users clicks on one link, the md file is shown on a new tab  

```

### Step 3: Run and verify 

verify on local and EC2 hosted. Confirm it works for both. 

