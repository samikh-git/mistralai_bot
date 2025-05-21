import praw
import os 
from mistralai import Mistral

api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-large-latest"

client = Mistral(api_key=api_key)

client_id = os.environ["CLIENT_ID"]
client_secret = os.environ["CLIENT_SECRET"]
password = os.environ["PASSWORD_REDDIT"]

reddit = praw.Reddit(
    client_id= client_id,
    client_secret= client_secret,
    password= password,
    user_agent="mistralai-bot/01 (by u/mistralai_bot)",
    username="mistralai_bot",
)

def main():
    return 

