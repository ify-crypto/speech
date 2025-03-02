import streamlit as st
#import speech_recognition as sr
#import pyttsx3
import time
import pandas as pd

# Create a tra nscibe_speech

def transcribe_speech():
    # Initialize recognizer class
    r = sr.Recognizer()

    # Reading Microphone as source
    with sr.Microphone() as source:         #--------Opens the microphone as the input audio source using
                                            #--This ensures that the microphone is properly initialized and closed after recording.

        # create a streamlit spinner that shows progress
        # to display a loading message indicating that background noise calibration is in progress.
        with st.spinner(text='Silence pls, Caliberating background noise.....'):
            time.sleep(2)

        # listens to the surrounding noise for 1 second and adjusts the recognizer’s sensitivity accordingly.

        r.adjust_for_ambient_noise(source, duration = 1) # ..... Adjust the surrounding noise
        st.info("Speak now...")

        audio_text = r.listen(source) #........................ listen for speech and store in audio_text variable
        with st.spinner(text='Transcribing your voice to text'):
            time.sleep(2)
        try:
            # using Google speech recognition to recognise the audio
            text = r.recognize_google(audio_text)
            # print(f' Did you say {text} ?')
            return text
        except:
            return "Sorry, I did not get that."
        

st.image('pngwing.com.png',caption = 'SPEECH RECOGNITION APP',width = 400)
st.markdown('<hr><hr><br>', unsafe_allow_html=True)

def main():
    st.title ("Speech Recognition App")
    st.write("Click on the microphone to start speaking:")

    # add a button to trigger speech recognition 
    if st.button('Start Recording'):
        your_words_in_text = transcribe_speech()
        st.write("Transcription: ", your_words_in_text)
if __name__ == "__main__":
    main()
