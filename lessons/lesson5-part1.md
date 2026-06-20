
# Make Nimbus into a Streamlit web app - using AI

In this step, you will convert the code inside the `notebooks/` folder into a simple web app using **Streamlit**.

Streamlit lets you create a web UI directly in Python.

---

## Step 1: Create an `app` folder

From the root of your repo:

```bash
cd smu-cce
mkdir app
```

---

## Step 2: Describe what you want 

Use this prompt in Copilot:

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

## Step 3: Run the app  

### Install dependencies

```bash
pip install -r requirements.txt
```

If Streamlit is not already included:

```bash
pip install streamlit
```

---

### Run the Streamlit app

```bash
python3 -m streamlit run app/app.py
```

---

### Open the app

In Codespaces, open the forwarded port shown by Streamlit.

Usually Streamlit runs on:

```text
http://localhost:8501
```

## Step 4: Edit the code (if needed)

If there are errors / problems use AI to problem solve. 