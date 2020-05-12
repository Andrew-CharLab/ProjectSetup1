import sys
import os
from github import Github
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

path = os.getenv("GTFILEPATH") # add projects dirctory from the env vars
gtusername = os.getenv("GTUSERNAME")
gtpassword = os.getenv("GTPASSWORD")

foldername = str(sys.argv[1])
_dir = path + '/' + foldername

g = Github(gtusername,gtpassword)
user = g.get_user()
login = user.login

repo = user.create_repo(foldername)

commands = [f'echo "# {repo.name}" >> README.md',
            'git init',
            f'git remote add origin https://github.com/{login}/{foldername}.git',
            'git add .',
            'git commit -m "Initial commit"',
            'git push -u origin master']

os.mkdir(_dir)
os.chdir(_dir)

for c in commands:
    os.system(c)

    print(f'{foldername} created locally')
    os.system('code .')

print("create <fldername>")
