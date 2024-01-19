import os
import browser_cookie3
from rich import print
from bardapi import BardCookies
from bardapi import ChatBard
from dotenv import load_dotenv
from rich.markdown import Markdown
from rich.console import Console


# Load environment variables from the .env file for secure access
load_dotenv()

# Create a Console instance for rich text printing
console = Console()

# https://bard.google.com
# pip install bardapi
# https://github.com/dsdanielpark/Bard-API

# ---------------------------- First Method ---------------------------- #
# Manually pass Bard Cookies in the cookie_dict

# create dictionary for the Bard cookies
# cookie_dict = {
#   "__Secure-1PSID": "fekfjlkfblblba-9ng774hwfe-6sjnk4jnkjn28ongj2nb3ujkn3479hkjn34ubgelQ.",
#   "__Secure-1PSIDTS": "CjIBPVxjSmEVl0JSwrfFtfuNBYiITiouhEl8z6jIpxSK1ZQqkoeIkkeykQ06WGaZz0RAA",
#   "__Secure-1PSIDCC": "ABTWhfweflnwlefw-94381yqwsA-MSXodr9GyFjkfesfs6GSsuvKZSWcp9Pd8jhsjZTa0O"
# }

# ---------------------------- Second Method ---------------------------- #
# Get Bard Cookies from environmental variable and pass it to cookie_dict

# create dictionary for the Bard cookies
# cookie_dict = {
#     "__Secure-1PSID": os.getenv("__Secure-1PSID"),
#     "__Secure-1PSIDTS": os.getenv("__Secure-1PSIDTS"),
#     "__Secure-1PSIDCC": os.getenv("__Secure-1PSIDCC")
# }

# ---------------------------- Third Method ---------------------------- #
# Fetch Cookie from Browser via Python

# Retrieve cookies from the Chrome browser using browser_cookie3 library
# Set the domain_name parameter to ".google.com" to filter cookies for that domain
# cookies = list(browser_cookie3.safari(domain_name=".google.com"))
cookies = list(browser_cookie3.chrome(domain_name=".google.com"))

# Create a dictionary comprehension to extract the cookie name and value pairs
# and store them in a dictionary called bard_cookies
bard_cookies = {cookie.name: cookie.value for cookie in cookies}

# # This is the test code only to print cookies values
# # print(bard_cookies.get('__Secure-1PSID'))
# # print(bard_cookies.get('__Secure-1PSIDTS'))
# # print(bard_cookies.get('__Secure-1PSIDCC'))

# create dictionary for the Bard cookies
cookie_dict = {
    "__Secure-1PSID": bard_cookies.get('__Secure-1PSID'),
    "__Secure-1PSIDTS": bard_cookies.get('__Secure-1PSIDTS'),
    "__Secure-1PSIDCC": bard_cookies.get('__Secure-1PSIDCC')
}

# bard = BardCookies(cookie_dict=cookie_dict)
bard = BardCookies(cookie_dict)

# ------------------ Text Summarization and Bullet Points ------------------ #
# text = '''The Earth is at a critical juncture as climate change accelerates. 
# Rising temperatures, extreme weather events, and melting ice caps threaten 
# ecosystems and human well-being. Immediate global cooperation is essential to
# reduce carbon emissions, transition to renewable energy, and preserve the planet
# for future generations. Let's unite to combat climate change and safeguard the 
# only home we have.'''

# bard_response = bard.get_answer(f"Summarize this {text} in a few sentences.")["content"]
# # bard_response = bard.get_answer(f"Summarize this {text} in a bullets points.")["content"]
# print(bard_response)
# md_response = Markdown(bard_response)
# console.print(md_response)

# ------------------ Language Translation ------------------ #
# text_to_translate = "you are awesome"
# target_language = "Hindi"
# translation = bard.get_answer(f"Translate this into {target_language}: {text_to_translate}")["content"]
# md_response = Markdown(translation)
# console.print(md_response)
# print(translation)

# ------------------ Write a Blog Post ------------------ #
# prompt = "write blog post for 'How to get started with Artificial Intelligence'"
# bard_response = bard.get_answer(prompt)
# print(bard_response["content"])

# ------------------ Image to Text ------------------ #
# # Read image and provide details
# with open('HumanRobots.jpeg', 'rb') as f: # (jpeg, png, webp) are supported.
#     image = f.read()
    
# bard_answer = bard.ask_about_image('What is in the image?', image)
# print(bard_answer['content'])

# # Read the text from the image 
# with open('hardtoread.webp', 'rb') as f:
#     # https://www.reddit.com/r/Handwriting/comments/y91fo9/i_often_dont_recognize_my_own_handwriting_and/
#     image_file = f.read()

# bard_response = bard.ask_about_image('can you please re-write this text present on this image?', image_file)
# print(bard_response['content'])

# Note: This functionality is only available for accounts with image upload capability in Bard's web UI.

# ------------------ Text To Speech(TTS) ------------------ #
audio = bard.speech('thank you for watching this video, hope you learnt something new and if you did, please do like, share and subscribe to my channel')
audio_file = 'my_audio.ogg'

with open(audio_file, "wb") as f:
  f.write(bytes(audio['audio']))

print(f'{audio_file} has been saved.')

# ------------------ Watch YouTube Video ------------------ #
# prompt = "can you please watch this video and summarise in text https://www.youtube.com/watch?v=NbEbs6I3eLw"
# bard_response = bard.get_answer(prompt)
# print(bard_response["content"])

# prompt = "can you please watch this https://www.youtube.com/watch?v=vk_s-gDTqkM youtube video and provide me the python code used in this video."
# bard_response = bard.get_answer(prompt)["content"]
# md_response = Markdown(bard_response)
# console.print(md_response)

# ------------------ Chat with Bard API  ------------------ #
# chat = ChatBard(token=bard_api_key)
# # print(chat._get_api_key)
# chat.start()

# ------------------ Generate Code with Bard API  ------------------ #
# prompt = "Write a Python code for the beginner without any explaination."
# bard_response = bard.get_answer(prompt)
# md_response = Markdown(bard_response.get('content'))
# console.print(md_response)

# ------------------ Error Handling with Bard API ------------------ #

# prompt = "write a simple 4 lines code in python with no explaination"

# try:
#     bard_response = bard.get_answer(prompt)
    
#     if bard_response.get('status_code') == 200:
#         # print(bard_response.get('content'))

#         console = Console()
#         # console.print(bard_response.get('content'))
        
#         markdown_output = Markdown(bard_response.get('content'))
#         console.print(markdown_output)
#         print('\n')
        
# except Exception as e:
#     print(f"An error occurred: {e}")







