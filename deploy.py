import os, shutil, time

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
    time.sleep(2)
    os.system("git add .")
    os.system("git commit -m 'deploy'")
    os.system("git checkout deploy")

    delete_files()

    os.system("git checkout main -- public")
    os.system("xcopy /s public . /Y")
    time.sleep(2)

    shutil.rmtree('public')
    time.sleep(2)

    os.system("git add .")
    os.system("git commit -m 'deploy-test'")
    os.system("git push")
    os.system("git checkout main")
    os.system("git push")
