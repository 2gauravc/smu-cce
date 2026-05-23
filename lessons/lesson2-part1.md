# Step-1 Open a Github Account with your SMU email ID 

Most of you who have taken the core course `Data Analytics for Economics` will already have this. You can directly skip to Step 2. 

## Github Student Developer Pack Registration

This guide explains how to apply for the Github Student Developer Pack using your SMU email account.

## Task 1: Sign In

Start at: https://github.com/settings/education/benefits

Log in using your SMU email by clicking **Continue with Google**.
Use your SMU email **without the faculty name**.

Example:
If your Outlook email is:

```text
abc.efg.2022@economics.smu.edu.sg
```

Sign in using:

```text
abc.efg.2022@smu.edu.sg
```

Complete:
- Password entry
- Captcha verification

---

## Task 2: Start the Application

Click:

```text
Start an application
```

Select:
- **Student**
- **Singapore Management University (SMU)**

Click:

```text
Select this school
```

Grant the required location permissions when prompted.

Then click:

```text
Continue
```

---

## Task 3: Verification

Upload a screenshot of your unofficial transcript for verification.

After uploading:
1. Press **OK**
2. You should be redirected to the dashboard
3. Your application status should show as **Submitted**

---

## Task 4: If Your Application Is Rejected (Optional)

If your application is rejected, Github will send you an email with instructions.

Typically, you should:

1. Enable two-factor authentication (2FA)
2. Complete Github billing profile information
3. Ensure your Github profile name matches your academic records

After completing the required steps:

1. Log out of Github
2. Log back in
3. Repeat Steps 1–3

---

## Task 5: Approval Confirmation

Your application is successful once you see the status:

```text
Approved
```

Note: Benefits may take up to 72 hours to become fully available after approval.


# Step 2: Start a Cloud VM on Github Codespaces 

Github Codespaces provides a cloud-based VM with a development environment that runs entirely in your browser. So goodbye to all installation hassles ! 

---

## What You Need Before Starting

Before creating a Codespace, ensure that:

- You have created a Github account
- You have successfully signed in
- Your Github Student Developer Pack application is approved (recommended)

---

## Open Github Codespaces

Go to: https://github.com/codespaces

---
## Create a New Codespace

Under `Explore quick start templates` choose the `Blank Template` 

Click:
```text
Use this template
```

## Wait for the VM to Start

Github will now create your cloud VM. This may take a few minutes the first time.

Once ready, you should see:

- VS Code running in your browser
- A terminal window
- A Linux-based cloud development environment

---
## Verify the VM Is Running

In the terminal, run:

```bash
python --version
```

You should see a Python version displayed.

Example:

```text
Python 3.12.x
```

## What You Now Have

You now have:
- A cloud-based Linux VM 
- VS Code running in the browser
- A development environment for coding and running applications

This VM runs in the cloud — not on your laptop.

---

## Important Notes

- Closing the browser does not delete your VM
- Your work can be saved and resumed later
- Codespaces automatically manages the development environment for you
- Codespaces will stop the VM after a period of inactivity. This saves cost 

---

## Step 3: Fork the Repository, Clone Your Copy, Install, and Run the Application

In this step, you will:
- Fork a copy of the instructor's Nimbus repository into your own Github account
- Clone the repo from the Github coud repo into the cloud VM
- Install the required software packages
- Run the application

---

## Fork the Repository

Open the instructor’s repository link.

Example:

```text
https://github.com/2gauravc/smu-cce
```

Click the **Fork** button at the top-right corner.

Github will create your own copy of the repository under your account.

Example:

```text
https://github.com/<your-username>/<repo-name>
```

---

## Open the Terminal

Inside Github Codespaces, open the terminal.

You can use:

```text
Terminal → New Terminal
```

---

## Clone Your Repository

Run the following command using **your forked repository URL**:

```bash
git clone https://github.com/<your-username>/smu-cce.git
```

Example:

```bash
git clone https://github.com/johnsmith/smu-cce.git
```

---

## Navigate to the Project Folder

After cloning completes, navigate to the project folder:

```bash
cd smu-cce/
```

---

## Verify the Files

Run:

```bash
ls
```

You should see project files and folders.

Example:

```text
README.md
requirements.txt
notebooks/
src/
```

---

## Install the Required Packages

Run:

```bash
pip install -r requirements.txt
```

This installs the Python libraries needed for the application.

The installation may take a few minutes.

---


## Open the Notebook

In the left hand Explorer bar, click on notebooks/ folder and open the `filings.ipynb` notebook.

```text
notebooks/filings.ipynb
```
---

## Run the Notebook

Inside the notebook:

1. Select the first cell
2. Click:

```text
Run
```

3. Continue running the cells one-by-one

---

## Verify the Code Is Working

You should see:
- Notebook output
- Charts / text / results
- Successful execution without errors

---




