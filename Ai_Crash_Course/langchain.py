# main.py
from secret_key import openapi_key
import os
from langchain_openai import OpenAI

# set your OpenAI API key
os.environ["OPENAI_API_KEY"] = openapi_key

# initialize the LLM
llm = OpenAI(temperature=0.6)

# generate a response
response = llm.invoke("I want to open a restaurant for Indian food. Suggest a fancy name for this")

# print the response
print("Suggested name:", response)






