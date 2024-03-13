Step 1: Set Up Gemini Pro API <br />
  a. Visit Google Ai Studio <br />
  b. Click the Get API Key in Google Studio Ai <br />
  c. Click Get API Key <br />
  d. Create the API key.<br />
  e. Copy the key <br />
<br />
Step2: Set up Microsoft Azure Speech Resource by visitng [here](https://portal.azure.com/#create/Microsoft.CognitiveServicesSpeechServices) <br />
  <br />
Step 3: Creating .env File <br />
  Create the File: Open a text editor and create a new file. Save it with the name .env and in the same root folder where you have cloned this repository. Ensure no file extension (like .txt) and the file starts with a dot. <br />
  Add Environment Variables: In the .env file, you can define your environment variables. For example: <br />
  GOOGLE_API_KEY=your_google_api_key<br />
  SPEECH_KEY=your-Microsoft-Azure-SpeechResource-Key <br />
  SPEECH_REGION=Microsoft-Azure-SpeechResource-Region <br />
<br />
Step 4: Initialize the Venv <br />
  a. Create ./venv (Vrtial environment)<br />
    conda create -p ./venv python=3.11 -y <br />
  b. Activate the environment<br />
    conda activate ./venv <br />
  <br />
Step 5: Crafting requirements.txt <br />
  a. Create a requirements.txt file <br />
    touch requirements.txt <br />
  b. streamlit<br />
    google-generativeai <br />
    python-dotenv <br />
    gtts <br />
    azure.cognitiveservices.speech<br />
    And save the above packages. <br />
  c.Installing the packages <br />
  pip install -r requirements.txt <br />
<br />
Finally, run streamlit run logy_app2.py in terminal.
