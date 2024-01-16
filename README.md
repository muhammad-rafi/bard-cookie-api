# Bard APIs via Cookies - Unoffical Way

---

### Introduction
Bard is designed as an interface to an LLM that enables users to collaborate with generative AI. We believe one of the promises of LLM-based innovations like Bard is to help people unlock their human potential so they can augment their imagination, expand their curiosity, and enhance their productivity. Read [here](https://ai.google/static/documents/google-about-bard.pdf) for more information.

To run these script, visit https://bard.google.com and login with your gmail account. Once logged in, on this page itself, right click and select 'Inspect', then go Application >> Cookies under https://bard.google.com cookies, when you get there find the cookie name '__Secure-1PSID' copy the value and save it as environmental variable or define in the script, this cookie will act as Bard API key.

You will need to install the Bard API unofficial library https://github.com/dsdanielpark/Bard-API

```
$ pip install bardapi
```

In addition to that, you may also need 'rich' library to get the mardown output, 'browser-cookie3' to fetch the cookie from browser and 'python-dotenv' to load the environmental variable to your python scripts.

```
pip install rich browser-cookie3 python-dotenv
```

Alternative, you can install the required libraries via requirements.txt present in this repo.

```
$ pip install -r requirements.txt
```
**Note: Please note that Bard-API is an unofficial python package that returns response of Google Bard through cookie value.**

### Setting Up a Virtual Environment

For better isolation and to avoid conflicts with your system-wide Python installation, it is recommended to use a Python virtual environment. Here are the steps:

1. Open a terminal in the project directory.
2. Create a virtual environment:

```bash
python3 -m venv venv
```

3. Activate the virtual environment:

- On Windows:

```bash
venv\Scripts\activate
```

- On macOS/Linux:

```bash
source venv/bin/activate
```

4. Install project dependencies:

```bash
pip install -r requirements.txt
```

### Running the Scripts

Now that you have set up a virtual environment, you can run the scripts. Make sure to activate the virtual environment before executing any commands.

```bash
# Example script execution command
python bardapi_with_single_cookie.py
```

## Environment Variables

You will need a `.env` file to define the variables for the followings

```bash
_BARD_API_KEY="<__Secure-1PSID cookie value>"
__Secure-1PSID="<__Secure-1PSID cookie value>"
__Secure-1PSIDTS="<<__Secure-1PSIDTS cookie value>"
__Secure-1PSIDCC="<__Secure-1PSIDCC cookie value>"
```


### ISSUES

If you find any issues with these scripts or have any suggestions, please do raise the issue or pull requests.

## Useful Links

- [An overview of Bard](https://ai.google/static/documents/google-about-bard.pdf)
- [Google Bard](https://bard.google.com/chat)
- [Bard-API - Unofficial ](https://github.com/dsdanielpark/Bard-API)
- [Introducing Bard - Sundar Pichai](https://blog.google/technology/ai/bard-google-ai-search-updates/)
- [Google Colab](https://colab.research.google.com)

### Authors

[Muhammad Rafi](https://github.com/muhammad-rafi)

### License

The source code is released under the [MIT](https://choosealicense.com/licenses/mit/).

### Credits

[Bard-API](https://github.com/dsdanielpark/Bard-API), created by [MinWoo(Daniel) Park
](https://github.com/dsdanielpark).