import os, shutil

def delete_files():
    for filename in os.listdir():
        if filename == ".git":
            continue
        if os.path.isdir(filename):
            shutil.rmtree(filename)
        elif os.path.isfile(filename):
            os.remove(filename)


if __name__ == "__main__":
    os.system("hugo -D")
    os.system("git add .")
    os.system("git commit -m 'deploy'")
    os.system("git checkout test")

    delete_files()

    os.system("git checkout main -- public")
    os.system("xcopy /s public . /Y")

    shutil.rmtree('public')

    os.system("git add .")
    os.system("git commit -m 'deploy-test'")
    os.system("git push")
    os.system("git checkout main")