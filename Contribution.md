# Run Locally

## Steps to Run the Project Locally

### 1. Fork the Repository
First, fork the repository to your GitHub account. You can do this by clicking the "Fork" button in the upper right corner of the repository page. This will create a copy of the repository in your account.

### 2. Clone the Forked Repository
Next, clone the forked repository to your local machine. Open a terminal and run the following command:

```bash
git clone https://github.com/DeepeshKalura/Trip-Planner
```

This will create a local copy of the repository on your machine.

### 3. Navigate to the Project Directory
Navigate to the directory of the cloned repository using the `cd` command:

```bash
cd Trip-Planner
```

### 4. Install All Necessary Packages
Install all the necessary Python packages. You can do this by running the following command:

```bash
pip install -r requirements.txt
```

This will install all the required packages listed in the `requirements.txt` file.

### 5. Download the SpaCy Model
Download the SpaCy model required for the project. Run the following command:

```bash
python -m spacy download en_core_web_sm
```

This will download and install the English language model for SpaCy.

### 6. Run the Streamlit Code
Finally, you can run the Streamlit code to launch the application. Use the following command:

```bash
streamlit run app.py
```

This command will start a local server and launch the Streamlit application. You can then access the application in your web browser by navigating to the specified URL.

That's it! You should now be able to run the project locally and interact with it using Streamlit.

