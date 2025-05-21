import praw
import os
from mistralai import Mistral

#Reddit bot that answers questions on a selected subreddit (defualt = "AskReddit")

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

QUESTIONS = ["what is", "who is", "what are"]
REPLY_TEMPLATE = "Hi! I am u/mistralai_bot a Reddit bot that can answer your questions using Mistral AI. \n"

def main(subreddit_name = "AskReddit"):
    """ Main function that goes runs the bot. Finds first applicable post and then asks to proceed."""
    subreddit = reddit.subreddit(subreddit_name)
    for submission in subreddit.stream.submissions():
        if len(submission.title.split()) < 10: 
            if process_submission(submission):
                proceed = input("Do you wish to proceed? [yes]/[no] ")
                if not "y" in proceed: 
                    print("FINISHED")
                    return 
    print("SUCCESS")

def process_submission(submission):
    """ Processes a submission and responds to it using the Mistral AI API.

    SUBMISSION: a submission object from the Reddit API"""
    normalized_title = submission.title.lower()
    for question in QUESTIONS: 
        if question in normalized_title:
            chat_response = client.chat.complete(
                model = model,
                messages = [
                    {
                        "role": "user",
                        "content": normalized_title,
                    },
                ]
            )
            reply_text = REPLY_TEMPLATE + chat_response.choices[0].message.content
            print(reply_text)
            submission.reply(reply_text)
            return True
    return False  