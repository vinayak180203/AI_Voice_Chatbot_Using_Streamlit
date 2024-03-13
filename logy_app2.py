import streamlit as st
import google.generativeai as genai
from gtts import gTTS
import tempfile
import base64
import azure.cognitiveservices.speech as speechsdk
import os

GOOGLE_API_KEY=os.environ.get('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

model=genai.GenerativeModel("gemini-pro") 
def text_to_speech(text):
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts = gTTS(text=text, lang='en')
        tts.save(f"{fp.name}.mp3")
        with open(f"{fp.name}.mp3", "rb") as audio_file:
            audio_data = audio_file.read()
            audio_base64 = base64.b64encode(audio_data).decode("utf-8")
            return audio_base64

def truncate_and_complete_response(response, max_length):
    if len(response) > max_length:
        truncated_response = response[:max_length]
        last_sentence_boundary = truncated_response.rfind('.')
        if last_sentence_boundary != -1:
            truncated_response = truncated_response[:last_sentence_boundary + 1]
        return truncated_response
    else:
        return response

recognized_text = ""
speaker_id = ""
current_audio = None
def play_audio(audio_base64):
    global current_audio
    if current_audio:
        return 
    current_audio = f'<audio src="data:audio/mp3;base64,{audio_base64}" autoplay="autoplay" controls="controls" style="display:none;"></audio>'
    st.write(current_audio, unsafe_allow_html=True)
    current_audio = None

def recognize_speech():
    global recognized_text, speaker_id
    recognized_text = ""
    speaker_id = ""  
    speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))
    speech_config.speech_recognition_language = "en-US"

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)  
    conversation_transcriber = speechsdk.transcription.ConversationTranscriber(speech_config=speech_config, audio_config=audio_config)

    def transcribed_cb(evt: speechsdk.SpeechRecognitionEventArgs):
        global recognized_text, speaker_id
        if evt.result.reason == speechsdk.ResultReason.RecognizedSpeech:
            print('\tText={}'.format(evt.result.text))
            print('\tSpeaker ID={}'.format(evt.result.speaker_id))
            recognized_text = evt.result.text
            speaker_id = evt.result.speaker_id

    conversation_transcriber.transcribed.connect(transcribed_cb)

    conversation_transcriber.start_transcribing_async()

    is_audio_playing = False
    while True:
        if recognized_text:
            user_query, speaker_name = recognized_text, speaker_id
            
            recognized_text = ""

            if not is_audio_playing and user_query:
                st.write(f"User: {user_query}")
                response = st.session_state.chat.send_message(user_query) 
                print(speaker_name)
                truncated_response = truncate_and_complete_response(response.text, 200)
                st.write(f"Gemini: {truncated_response}")
                audio_base64 = text_to_speech(truncated_response)
                play_audio(audio_base64)
                is_audio_playing = True

            elif is_audio_playing and user_query and speaker_name=="Guest-2":
                continue

            elif is_audio_playing and user_query and speaker_name!="Guest-2":
                is_audio_playing = False
                # Send user's query to the model
                st.write(f"User: {user_query}")
                response = st.session_state.chat.send_message(user_query) 
                print(speaker_name)
                truncated_response = truncate_and_complete_response(response.text, 200)
                st.write(f"Gemini: {truncated_response}")
                audio_base64 = text_to_speech(truncated_response)
                play_audio(audio_base64)
                is_audio_playing = True
               
def role_to_streamlit(role):
  if role == "model":
    return "assistant"
  else:
    return role

if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history = [])

st.title("Chat with Google Gemini-Pro!")

for message in st.session_state.chat.history:
    with st.chat_message(role_to_streamlit(message.role)):
        st.markdown(message.parts[0].text)

recognize_speech()