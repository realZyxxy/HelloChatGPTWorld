import openai
import os

###############################################################################
# A Medium article that describes this project is here:
# https://medium.com/@real.zyxxy/hello-chatgpt-world-run-chatgpt-inside-a-python-script-in-5-minutes-4c9f4bdb6e28

###############################################################################
# do change these values - they are the parameters of ChatGPT request
###############################################################################

prompt = "Hello, the brave new ChatGPT world!" # That's your chat prompt
# You can change its value - ask ChatGPT anything you like.

temperature = 0.9 # temperature's value must be a number between 0.0 and 1.0, 
# 0.0 being the most deterministic, consistent ChatGPT mode,
# and 1.0 being the most randon, unpredictable, creative ChatGPT mode.

###############################################################################
# technical part - it informs the package about your OpenAI API key
###############################################################################
# you need to get your personal OpenAI API key, 
# then assign its value to
# a secret (system variable) OPENAI_API_KEY. 
# It will only take a few minutes, and there is no need to pay money, 
# or share your bank card details.
# Then, save it as a secret named OPENAI_API_KEY . Instructions here ->
# https://docs.replit.com/programming-ide/workspace-features/storing-sensitive-information-environment-variables

if "OPENAI_API_KEY" not in os.environ:
  raise Exception("You need to assign your your OpenAI API key to system variable (Replit's secret) named 'OPENAI_API_KEY'. It will only take a few minutes, and there is no need to pay money, or share your bank card details. See details in the comments.")
openai.api_key = os.getenv('OPENAI_API_KEY')

###############################################################################
# technical part - we call ChatGTP and print its response.
###############################################################################
long_response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": 'user', "content": prompt}],
    temperature=temperature # a number between 0 and 1
    # temperature is the degree of randomness of the model's output
  )
response = long_response.choices[0].message["content"]

print(f"""You: "{prompt}"\nChatGPT: "{response}" """)
