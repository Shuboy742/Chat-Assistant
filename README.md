# Chat-Assistant
**Project Description: Research Assistant with Hugging Face and LangChain
This project is a simple Research Assistant web app built using Streamlit, LangChain, and Hugging Face models.
Users can enter any research prompt, and the app will generate a relevant, AI-powered response using a large language model (e.g., Llama-3.1-8B-Instruct) hosted on Hugging Face.**

Key Features:
User-friendly web interface (Streamlit)
Utilizes state-of-the-art Hugging Face language models via LangChain
Easily customizable for different models or tasks

Setup Instructions
1. Clone or Download the Project
Place your promptui.py file in a folder.

2. Create and Activate a Virtual Environment (Recommended)
python3 -m venv venv
source venv/bin/activate

3. Install Required Packages
pip install streamlit langchain-huggingface python-dotenv
pip install -r requirements.txt

4. Set Your Hugging Face API Token
Go to https://huggingface.co/settings/tokens and copy your token.
Create a .env file in your project folder with this line:
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token_here

5. Run the App
Open the URL shown in your terminal (usually http://localhost:8501).
