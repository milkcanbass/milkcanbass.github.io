import os
import openai

openai.api_key = os.getenv('OPENAI_API_KEYS')
from git import Repo
from pathlib import Path

PATH_TO_BLOG_REPO = Path("/Users/shintarokai/Dev/Python/OpenAi/milkcanbass.github.io/.git")
PATH_TO_BLOG = PATH_TO_BLOG_REPO.parent
PATH_TO_CONTENT = PATH_TO_BLOG/"content"
PATH_TO_CONTENT.mkdir(exist_ok=True,parents=True)

def update_blog(commit_message='pdates blog'):
    # =GitPython -- Repor Location
    repo = Repo(PATH_TO_BLOG_REPO)
    #git add
    repo.git.add(all=True)
    # git commit -m "updates blog"
    repo.index.commit(commit_message)
    #git push 
    origin = repo.remote(name='origin')
    origin.push()
    
random_text_string = "testtest"
with open(PATH_TO_BLOG/"index.html",'w') as f:
    f.write(random_text_string)

update_blog()

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

if os.path.exists(PATH_TO_CONTENT):
    print(PATH_TO_CONTENT)
else:
    print("The directory does not exist.")
