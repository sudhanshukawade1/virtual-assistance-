import pyttsx3
import speech_recognition as sr
import webbrowser
import os
import datetime
import openai
import random
import yt_dlp
import langchain

from openai import OpenAI
# Initialize text-to-speech engine
engine = pyttsx3.init()
client = OpenAI()
#client.api_key="sk-proj-fwcf800YzIIIhf0qSguYT3BlbkFJtje5wKsMq44ppSpmhVCW"
# Function to speak text
def Say(text):
  """
  This function speaks the provided text using the text-to-speech engine.
  """
  engine.say(text)
  engine.runAndWait()


# Function to generate text for each section using OpenAI's API\
#OpenAI.api_key = apikey#
#def ai(prompt):
 #task = f"OpenAI response for prompt: {prompt}  \n *******************\n\n"
 #response = openai.completions.create(
  #  model="gpt-3.5-turbo-instruct",-
   # prompt=prompt,
    #max_tokens=500


 #print(response["choices"][0]["text"])
 ###  os.mkdir("Openai")

 #with open(f"Openai/prompt- {random.randint(1,2343434356)}","w") as f:
  #  f.write(task)

# Function to take voice command
def take_command():
  """
  This function listens for user's voice command and returns the recognized text.
  """
  recognizer = sr.Recognizer()
  with sr.Microphone() as source:
    print("Listening...")
    audio = recognizer.listen(source)
  try:
    query = recognizer.recognize_google(audio, language="en-in")
    print(f"User said: {query}")
    return query.lower()  # Convert to lowercase for case-insensitive matching
  except Exception as e:
    print("sorry sudhanshu I Could not recognize audio: " + str(e))
    Say ("sorry sudhanshu I Could not recognize audio: "  + str(e))
    return("sorry sudhanshu I Could not recognize audio: ")#+ str(e))
# Welcome message and listen for command
Say("Hello sudhanshu , I am your virtual assistant. How can I help you today?")

while True:
  # Get user command in lowercase for case-insensitive matching
  text = take_command()
  sites = [ ["youtube","https://www.youtube.com"],["wikipedia","https://www.wikipedia.com"],
          ["instagram", "https://www.instagram.com"],["google","https://www.google.com"] ]
  for site in sites:

    if f"open {site[0]}" in text:
     Say(f"Opening {site[0]} sir...")
     webbrowser.open(site[1])
     break

    elif "the time" in text:
     strfTime = datetime.datetime.now().strftime("%Hour:%Minutes:%Seconds")
     Say(f"sir the time is{strfTime} ")

    elif "using artificial intelligence" in text:
     ai(prompt=text)

    elif 'play' in text and 'song' in text:
     song_name = text.split("play")[1].strip()
     ydl_opts = {"format": "bestaudio/best"}  # Choose preferred audio format
     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
      try:
        info_dict = ydl.extract_info(f"ytsearch:{song_name}", download=False)  # Search and get info
        if 'entries' in info_dict:
          video_url = info_dict['entries'][0]['id']  # Get video URL from search results
          Say(f"Playing {song_name} for you...")
          break

        else:
          Say(f"Sorry, couldn't find a song titled '{song_name}'.")

      except yt_dlp.utils.DownloadError as e:
        Say(f"An error occurred while playing the song: {str(e)}")

