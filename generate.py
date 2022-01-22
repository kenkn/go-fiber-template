import os
import sys
import shutil
import subprocess

ARGS_ERROR_MESSAGE = 'usage: fiber-generate <project name> [project-dir]'

def validate_arg():
    if not (len(sys.argv) == 2 or len(sys.argv) == 3):
        print(ARGS_ERROR_MESSAGE)
        quit()

def run():
    validate_arg()
    project_name = sys.argv[1]
    if len(sys.argv) == 2:
        project_path = f'{os.getcwd()}/{project_name}'
    if len(sys.argv) == 3:
        project_dir = sys.argv[2]
        project_path = f'{project_dir}/{project_name}'
    
    command = [f'go mod init {project_name}-api' ,
               'go get -u github.com/gofiber/fiber/v2',
               'go get -u github.com/dgrijalva/jwt-go']
    try:
        shutil.copytree('./api', project_path)
    except FileExistsError:
        print(f"Project exists: '{project_name}'")
        quit()
    os.chdir(project_path)
    for c in command:
        subprocess.call(c.split())
    
    
if __name__ == '__main__':
    run()