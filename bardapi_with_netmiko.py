from bardapi import BardCookies
from netmiko import ConnectHandler
from rich.markdown import Markdown
from rich.console import Console
from getpass import getpass
import time
import browser_cookie3

'''

Make sure you are logged in to "https://bard.google.com/chat" first before 
you run this script and Google Chrome shouw be your default browser .

Python Libraries required
pip install getpass requests browser_cookie3 bardapi netmiko

https://github.com/dsdanielpark/Bard-API
Please exercise caution and use this package responsibly. This python package is UNOFFICIAL.

'''

def get_bard_cookies(domain_name=".google.com", browser="chrome"):
    """
    Obtains specified cookies from the specified browser using the browser_cookie3 library.

    Args:
        domain_name (str, optional): The domain name to filter cookies for. Defaults to ".google.com".
        browser (str, optional): The name of the browser to extract cookies from. Defaults to "chrome".

    Returns:
        dict or None: A dictionary containing the requested cookies, or None if no matching cookies were found.
    """

    try:
        # Use getattr to dynamically access the browser's cookie retrieval function
        cookies = list(getattr(browser_cookie3, browser)(domain_name=domain_name))

        bard_cookies = {cookie.name: cookie.value for cookie in cookies}

        cookie_dict = {
            "__Secure-1PSID": bard_cookies.get('__Secure-1PSID'),
            "__Secure-1PSIDTS": bard_cookies.get('__Secure-1PSIDTS'),
            "__Secure-1PSIDCC": bard_cookies.get('__Secure-1PSIDCC')
        }

        return cookie_dict if any(cookie_dict.values()) else None

    except AttributeError:
        print(f"Unsupported browser: {browser}")
        return None
    

def get_answer_from_bard(bard_cookies, prompt):
        """
        Retrieves an answer from Bard using the provided cookies and prompt.

        Args:
            bard_cookies (dict): A dictionary containing the cookies needed for Bard authentication.
            prompt (str): The prompt or question to ask Bard.

        Returns:
            str or None: The textual content of Bard's response, or None if an error occurred.

        Raises:
            Exception: If any errors occur during Bard interaction.
        """
        try:
            # Use the Bard Cookies to initialize Bard
            bard = BardCookies(cookie_dict=bard_cookies)

            # Now you can use Bard as before
            # prompt = "Write a nice greeting message."
            bard_response = bard.get_answer(prompt)

            # # Get other metadata
            # print(bard_response.keys())
            
            return bard_response.get("content")

        except Exception as error:
            print(f"Error: {error}")
            return None


def get_credentials():
    """
    Prompts the user for their username and password, and returns them as a tuple.

    Returns:
        tuple: A tuple containing the entered username and password.
    """
    username = input('Enter your username: ')
    password = getpass('password: ')
    return username, password


def execute_command(host, username, password, command, port=22):
    """
    Executes a command on a remote Cisco IOS device using SSH.

    Args:
        host (str): The hostname or IP address of the device.
        username (str): The username for SSH authentication.
        password (str): The password for SSH authentication.
        command (str): The command to execute on the device.
        port (int, optional): The SSH port number. Defaults to 22.

    Returns:
        str or None: The output of the executed command, or None if an error occurred.

    Raises:
        Exception: If any errors occur during the SSH connection or command execution.
    """
    device = {
        "device_type": "cisco_ios",
        "ip": host,
        "username": username,
        "password": password,
        "port": port,
    }

    try:
        # Establish an SSH connection
        with ConnectHandler(**device) as ssh_conn:
            output = ssh_conn.send_command(command)
        return output
    except Exception as e:
        print(f"Error: {e}")
        return None
    
        
if __name__ == '__main__':
    
    # Return the desired bard cookies from the Google Chrome Browser
    bard_cookies = get_bard_cookies(domain_name=".google.com", browser="chrome")

    username, password = get_credentials()
    host = 'sandbox-iosxe-latest-1.cisco.com'
    command = 'show version'
    
    # Executes the show command with netmiko
    command_output = execute_command(host, username, password, command)
    
    if command_output is not None:
        prompt = f"You are an expert network engineer and you have been asked to brief on the this command output: {command_output}."
        bard_response = get_answer_from_bard(bard_cookies, prompt)
        # print(bard_response)

        console = Console()
        # console.print(bard_response, markup=True)
        
        markdown_output = Markdown(bard_response)
        console.print(markdown_output, markup=True)
        
    else:
        print("Error executing the command.")
    