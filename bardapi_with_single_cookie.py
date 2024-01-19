from bardapi import Bard
from bardapi import ChatBard
from dotenv import load_dotenv
from browser_cookie3 import chrome
import os

# Load environment variables from the .env file for secure access
load_dotenv()

''' To run the script, visit https://bard.google.com and login with your gmail account,
Once logged in, on the page right click and select 'Inspect', then go Application >> Cookies, 
once you get there find the cookie name '__Secure-1PSID' copy the value and save this as environmental variable
or define in the script, this cookie will act as Bard API key.

You will also need to install the Bard API unofficial library https://github.com/dsdanielpark/Bard-API
$ pip install bardapi

Note: Please note that Bard-API is an unofficial python package that returns response of Google Bard through cookie value.
'''

# # Define the '__Secure-1PSID' as the token in the script 
# token = 'fAjCwabsgmsjA7J2MrDVkdyZ-Bxo2psnm6UPOJWKXerx9zWJZ7g.'
# bard = Bard(token=token)  

# ---------------- Token from Browser Cookie Manually ----------- #
# # Get Bard API from environmental variable
# bard_api_key = os.getenv("_BARD_API_KEY")

# # Define Bard API Token
# bard = Bard(token=bard_api_key)  

# prompt = "Write a 4 lines poem about the beauty of nature for 5 years old"

# bard_response = bard.get_answer(prompt)
# print(bard_response["content"])

# ------------------ Fetch Cookie from Browser via Python ------------------ #

# Extract the Key from Your Browser (if available)
# bard = Bard(token_from_browser=True)

# prompt = "Write a 4 lines poem about the beauty of nature for a 3 year old"
# bard_response = bard.get_answer(prompt)
# print(bard_response["content"])

# # Fetch all the cookies from Google Chrome browser and save them in a list
list_cookies = list(chrome(domain_name = ".google.com"))
bard_cookie = [cookie for cookie in list_cookies if cookie.name == "__Secure-1PSID"][0].value.strip()
# print(bard_cookie)
# print(bard_cookie.value.strip())

bard = Bard(token=bard_cookie)  
print(bard.get_answer("Do you like cookie ? ")["content"])

# ------------------ Text Summarization ------------------ #
# text = '''The Earth is at a critical juncture as climate change accelerates. 
# Rising temperatures, extreme weather events, and melting ice caps threaten 
# ecosystems and human well-being. Immediate global cooperation is essential to
# reduce carbon emissions, transition to renewable energy, and preserve the planet
# for future generations. Let's unite to combat climate change and safeguard the 
# only home we have.'''

# summary = bard.get_answer(f"Summarized Text: {text}")["content"]
# print(summary)

# ------------------ Language Translation ------------------ #
# text_to_translate = "Hello, how are you?"
# target_language = "Hindhi"
# translation = bard.get_answer(f"Translate this into {target_language}: {text_to_translate}")["content"]
# print(translation)

# ------------------ Write a Blog Post ------------------ #
# prompt = "write blog post for 'How to get started with Artificial Intelligence'"
# bard_response = bard.get_answer(prompt)
# print(bard_response["content"])

# ------------------ Image to Text ------------------ #
# with open('HumanRobots.jpeg', 'rb') as f: # (jpeg, png, webp) are supported.
#     image = f.read()
    
# bard_answer = bard.ask_about_image('What is in the image?', image)
# print(bard_answer['content'])

# Note: This functionality is only available for accounts with image upload capability in Bard's web UI.

# ------------------ Watch YouTube Video ------------------ #
# prompt = "can you please watch this video and summarise in text https://www.youtube.com/watch?v=NbEbs6I3eLw"
# bard_response = bard.get_answer(prompt)
# print(bard_response["content"])

# ------------------ Chat with Bard API  ------------------ #
# chat = ChatBard(token=bard_api_key)
# # print(chat._get_api_key)
# chat.start()

# ------------------ Text To Speech(TTS) ------------------ #
# audio = bard.speech('thank you for watching this video, hope you learnt something new and if you did, please do like, share and subscribe to my channel')
# audio_file = 'my_audio.ogg'

# with open(audio_file, "wb") as f:
#   f.write(bytes(audio['audio']))

# print(f'{audio_file} has been saved.')
