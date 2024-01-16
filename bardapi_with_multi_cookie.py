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

# # https://bard.google.com
# # pip install bardapi
# # https://github.com/dsdanielpark/Bard-API


# ---------------------------- First Method ---------------------------- #
# # Get Bard Cookies from environmental variable and 
# # create dictionary for the Bard cookies
# cookie_dict = {
#     "__Secure-1PSID": os.getenv("__Secure-1PSID"),
#     "__Secure-1PSIDTS": os.getenv("__Secure-1PSIDTS"),
#     "__Secure-1PSIDCC": os.getenv("__Secure-1PSIDCC")
# }

# ---------------------------- Second Method ---------------------------- #
cookies = list(browser_cookie3.chrome(domain_name = ".google.com"))
bard_cookies = {cookie.name: cookie.value for cookie in cookies}

# This is the test code only to print cookies values
# print(bard_cookies.get('__Secure-1PSID'))
# print(bard_cookies.get('__Secure-1PSIDTS'))
# print(bard_cookies.get('__Secure-1PSIDCC'))

cookie_dict = {
    "__Secure-1PSID": bard_cookies.get('__Secure-1PSID'),
    "__Secure-1PSIDTS": bard_cookies.get('__Secure-1PSIDTS'),
    "__Secure-1PSIDCC": bard_cookies.get('__Secure-1PSIDCC')
}

# bard = BardCookies(cookie_dict=cookie_dict)
bard = BardCookies(cookie_dict)
# prompt = "write a simple 4 lines code in python with no explaination"

with open('hardtoread.webp', 'rb') as f:
    # https://www.reddit.com/r/Handwriting/comments/y91fo9/i_often_dont_recognize_my_own_handwriting_and/
    image_file = f.read()

bard_response = bard.ask_about_image('can you please re-write this text present on this image?', image_file)
print(bard_response['content'])

try:
    bard_response = bard.get_answer(prompt)
    
    if bard_response.get('status_code') == 200:
        # print(bard_response.get('content'))

        console = Console()
        # console.print(bard_response.get('content'))
        
        markdown_output = Markdown(bard_response.get('content'))
        console.print(markdown_output)
        print('\n')
        
except Exception as e:
    print(f"An error occurred: {e}")







