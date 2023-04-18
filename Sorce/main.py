import os
import openai

openai.api_key = os.getenv('OPENAI_API_KEYS')
from git import Repo
from pathlib import Path

PATH_TO_BLOG_REPO = Path("/Users/shintarokai/Dev/Python/OpenAi/milkcanbass.github.io/.git")
PATH_TO_BLOG = PATH_TO_BLOG_REPO.parent
PATH_TO_CONTENT = PATH_TO_BLOG/"content"
PATH_TO_CONTENT.mkdir(exist_ok=True,parents=True)

def update_blog(commit_message='updates blog'):
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

import shutil
def create_new_blog(title,content,cover_image):
    cover_image = Path(cover_image)

    files = len(list(PATH_TO_CONTENT.glob(".html")))
    new_title = f"{files+1}.html"
    path_to_new_content = PATH_TO_CONTENT/new_title

    shutil.copy(cover_image,PATH_TO_CONTENT)

    if not os.path.exists(path_to_new_content):
        #write a new html file
        with open(path_to_new_content,"w") as f:
            f.write("<!DOCTYPE html>\n")
            f.write("<html>\n")
            f.write("<head>\n")
            f.write(f"<title> {title} </title>\n")
            f.write("</head>\n")
            
            f.write("<body>\n")
            f.write(f"<img src='{cover_image.name}' alt='Cover Image'> <br />\n")
            f.write(f"<h1> {title} </h1>")
            #Open AI --> Completion GPT --> "hello\nblog post \n"
            f.write(content.replace("\n", "<br />\n"))
            f.write("</body>\n")
            f.write("</html>\n")
            print("Blog created")
            return path_to_new_content
    else:
        raise FileExistsError("File already exists, check again your name")
   
path_to_new_content = create_new_blog('test_title','chikuwa','logo.png')

# Test GPT-3 completion
# prompt = "Once upon a time"
# model = "text-davinci-002"
# response = openai.Completion.create(
#     engine=model,
#     prompt=prompt,
#     max_tokens=50,
#     n=1,
#     stop=None,
#     temperature=0.5,
# )

# print(response.choices[0].text)

# if os.path.exists(PATH_TO_CONTENT):
#     print(PATH_TO_CONTENT)
# else:
#     print("The directory does not exist.")
