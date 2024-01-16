import google.generativeai as genai
from dotenv import load_dotenv
from rich.markdown import Markdown
from rich.console import Console
import os

# Load environment variables from the .env file
# to keep sensitive information out of the code
load_dotenv()

# Create a Console instance for rich text printing
console = Console()

# Fetch the Google Gemini API key from the environment variables
# for secure access and flexibility across different environments
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure the Generative AI API with the API key
genai.configure(api_key=GOOGLE_API_KEY)

# Load the Gemini Pro generative model
model = genai.GenerativeModel("gemini-pro")

# Initialize context object
context_obj = {"previous_user_queries": []}  # Store previous queries for context

# Present a welcome message
welcome_msg = '''****************************************************************************
****************** Welcome to AI ChatBot Using Gemini API ******************
****************************************************************************
Ask me any questions that spark your curiosity, or press Ctrl+C to exit'''
# print(f"\033[36m{welcome_msg}\033[0m", end="")

console.print(f"[cyan]{welcome_msg}[/cyan]")
print('\n')

# Initiate an interactive loop for continuous user interaction
while True:
    try:
        # # Clear and concise exit message (before prompt):
        # Simply type your questions below, or press Ctrl+C to exit gracefully.
        # console.print("[green]To quit, press Ctrl+C or type 'exit'.[/green]")

        query = input("You Question: ")

        # Add query to context
        context_obj["previous_user_queries"].append(query)
        
        # Generate a response from the Gemini model based on the user's query
        response = model.generate_content(query)

        # Print the generated response clearly labeled as the answer
        # print("Answer:", response.text + "\n")
        md_response = Markdown(response.text)
        # console.print(md_response)   
        console.print("Gemini Answer:", md_response)

        # Check for exit command to exit the loop
        if query.lower() == "exit":
            break

    except KeyboardInterrupt:
        console.print(f"\n[red]Exiting...[red]")  # Print exit message in red
        break 
    
    except Exception as e:
        console.print(f"[bold red]Error:", {e})  # Print error message in bold red

    console.print("\n")  # Add extra newline for visibility