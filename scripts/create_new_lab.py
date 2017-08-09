import os
from zipfile import ZipFile
import json
import platform


def op_system():
    '''
    Return underlying platform's OS
    '''
    if 'windows' in platform.platform().lower():
        return 'windows'
    else:
        return 'unix'

def create_dir():

    '''
    Creates folder structure for the LL and
    copies templates to the folder.
    '''
    root_dir = input("How would you like to name the root directory? ")
    os.makedirs(os.path.join('labs', root_dir))
    with ZipFile('templates.zip', 'r') as zip_file:
        zip_file.extractall('labs/'+root_dir)
    os.chdir('labs/'+root_dir)

    for file in os.listdir():
        if file.endswith('.json'):
            os.rename(file, root_dir+'.json')

    os.makedirs(os.path.join('assets', 'images'))
    with open(root_dir+'.json', 'r+') as json_file:
        data = json.load(json_file)
        data['labId'] = root_dir
        data['title'] = input("What is the title of the lab? ")
        data['slug'] = input("Provide a short description for the lab. ")
        data['time'] = input("Approximately how long will it take to complete the lab? ")
        data['tags'][0]['title']= input("Name the tag associated with this lab. ")
        data['authors'][0]['name']= input("What is the name of the author of this lab? ")
        data['authors'][0]['email']= input("What is author's email address? ")
        json_file.seek(0)
        json_file.write(json.dumps(data, indent=2, sort_keys=True))
        json_file.truncate()
    print("\n\n\nJSON file has been created, but it might need additional modification after the content is written.\n\n")

    print("The folder structure has been successfully created.\n")


    if op_system() == 'windows':
        os.system('cd ../../ && tree /A /F')
    else:
        os.system('cd ../../ && tree')

create_dir()
