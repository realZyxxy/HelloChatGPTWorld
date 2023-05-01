import openai
import os

###############################################################################
# do change these values - they are the parameters of ChatGPT request
###############################################################################

prompt = "Hello, the brave new ChatGPT world!" # That's your chat prompt
# You can change its value - ask ChatGPT anything you like.

temperature = 0.9 # temperature's value must be a number between 0.0 and 1.0, 
# 0.0 being the most deterministic, consistent ChatGPT mode,
# and 1.0 being the most randon, unpredictable, creative ChatGPT mode.

###############################################################################
# don't change this section - it informs the package about your OpenAI API key
###############################################################################
# you need to get your personal OpenAI API key, 
# then assign its value to
# a secret (system variable) OPENAI_API_KEY. 
# It will only take a few minutes, and there is no need to pay money, 
# or share your bank card details.

if "OPENAI_API_KEY" not in os.environ:
  raise Exception("You need to assign your your OpenAI API key to system variable (Replit's secret) named 'OPENAI_API_KEY'. It will only take a few minutes, and there is no need to pay money, or share your bank card details. See details in the comments.")
openai.api_key = os.getenv('OPENAI_API_KEY')

###############################################################################
# don't change this section - it calls ChatGTP and prints its response.
###############################################################################
long_response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": 'user', "content": prompt}],
    temperature=temperature # a number between 0 and 1
    # temperature is the degree of randomness of the model's output
  )
response = long_response.choices[0].message["content"]

print(f"""You: "{prompt}"\nChatGPT: "{response}" """)
