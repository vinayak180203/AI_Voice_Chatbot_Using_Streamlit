Step 1: Set Up Gemini Pro API
  a. Visit Google Ai Studio
  b. Click the Get API Key in Google Studio Ai
  c. Click Get API Key
  d. Create the API key.
  e. Copy the key

Step2: Set up Microsoft Azure Speech Resource by visitng [here](https://portal.azure.com/#create/Microsoft.CognitiveServicesSpeechServices)
  
Step 3: Creating .env File
  Create the File: Open a text editor and create a new file. Save it with the name .env and in the same root folder where you have cloned this repository. Ensure no file extension (like .txt) and the file starts with a dot.
  Add Environment Variables: In the .env file, you can define your environment variables. For example:
  GOOGLE_API_KEY=your_google_api_key
  SPEECH_KEY=your-Microsoft-Azure-SpeechResource-Key
  SPEECH_REGION=Microsoft-Azure-SpeechResource-Region

Step 4: Initialize the Venv
  a. Create ./venv (Vrtial environment)
    conda create -p ./venv python=3.11 -y
  b. Activate the environment
    conda activate ./venv
  
Step 5: Crafting requirements.txt
  a. Create a requirements.txt file
    touch requirements.txt
  b. streamlit
    google-generativeai
    python-dotenv
    gtts
    azure.cognitiveservices.speech
    And save the above packages.
  c.Installing the packages
  pip install -r requirements.txt
