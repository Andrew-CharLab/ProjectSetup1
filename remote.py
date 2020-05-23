import sys
import os
from github import Github
from dotenv import load_dotenv

#load .env file and put them into OS Enviroment Variables
load_dotenv()

#copy Enviroment Variables to local Variables
path = os.getenv("GTFILEPATH") # add projects dirctory from the env vars
gtusername = os.getenv("GTUSERNAME")
gtpassword = os.getenv("GTPASSWORD")

#set full path and folder name variables
foldername = str(sys.argv[1])
_dir = path + '/' + foldername

#connect to Github
g = Github(gtusername,gtpassword)
user = g.get_user()
login = user.login

#create github repo
repo = user.create_repo(foldername)

#do first time run init and file creation for project
commands = [f'echo "# {repo.name}" >> README.md',
            'git init',
            f'git remote add origin https://github.com/{login}/{foldername}.git',
            'git add .',
            'git commit -m "Initial commit"',
            'git push -u origin master']

#create project folder
os.mkdir(_dir)
print(f'{foldername} created locally')

#change to project folder
os.chdir(_dir)

#run first commands
for c in commands:
    os.system(c)

#tell the user what we did
print("create <fldername>")

#launch VSCode in current directory
os.system('code .')


