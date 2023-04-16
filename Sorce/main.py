import os
import openai

openai.api_key = os.getenv('OPENAI_API_KEYS')
from git import repo
from pathlib import Path

PATH_TO_BLOG_REPO = Path("/Users/shintarokai/Dev/Python/OpenAi/.git")


# Test GPT-3 completion
prompt = "Once upon a time"
model = "text-davinci-002"
response = openai.Completion.create(
    engine=model,
    prompt=prompt,
    max_tokens=50,
    n=1,
    stop=None,
    temperature=0.5,
)

# print(response.choices[0].text)

if os.path.exists(PATH_TO_BLOG_REPO):
    print("The directory exists!")
else:
    print("The directory does not exist.")
