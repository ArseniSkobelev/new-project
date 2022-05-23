# py new-project.py 'PROJECT NAME' 'PROJECT TYPE (1, 2, 3 etc.)'

import os
import sys
import shutil

from colorama import init, Fore, Back, Style

init(convert=True)

cwd = os.getcwd()

projectProperties = sys.argv

templateDirectory = os.path.dirname(
    os.path.realpath(sys.argv[0])) + "\Templates"


def main():

    # Welcome message
    welcomeString = """
                                                    _              _   
                                                   (_)            | |  
  _ __    ___ __      __ ______  _ __   _ __  ___   _   ___   ___ | |_ 
 | '_ \  / _ \\ \ /\ / /|______|| '_ \ | '__|/ _ \ | | / _ \ / __|| __|
 | | | ||  __/ \ V  V /         | |_) || |  | (_) || ||  __/| (__ | |_ 
 |_| |_| \___|  \_/\_/          | .__/ |_|   \___/ | | \___| \___| \__|
                                | |               _/ |                 
                                |_|              |__/                  
    """
    print(Fore.GREEN + welcomeString)
    # print(Style.RESET_ALL)

    try:
        stringInt = int(projectProperties[2])
    except ValueError:
        return print(Fore.RED + "Incorrect project type!")

    def createProject(projType, projName):
        print("Project name: " + projName)
        match projType:
            case "1":
                print("Project type: HTML, CSS and vanilla JS")
                shutil.copytree(templateDirectory +
                                "\VanillaJS", cwd + '/' + projName)
            case "2":
                print("Project type: HTML, CSS, vanilla JS and Tailwind.css")
                # copy_tree(templateDirectory +
                #           "\VanillaJSWithTailwind", cwd)
                # os.mkdir(cwd + '/' + projName)
                shutil.copytree(templateDirectory +
                                "\VanillaJSWithTailwind", cwd + '/' + projName)
            case "3":
                print("Project type: NodeJS")
                # os.system('cmd /c "npm init -y"')
            case "4":
                return print("ReactJS")

    createProject(projectProperties[2], projectProperties[1])

    # get directory from where the scipt was started


if __name__ == "__main__":
    main()
