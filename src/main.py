import os
import shutil

def main():
    print("Quiche Eater")
    copy_contents_to("/home/cmdfrog/workspace/github.com/cmdFrog/SSG/static", "/home/cmdfrog/workspace/github.com/cmdFrog/SSG/public")


def copy_contents_to(from_path, to_path):
    if os.listdir(to_path):
        shutil.rmtree(to_path)
        os.mkdir(to_path)
    file_dir = os.listdir(from_path)
    #current_path = from_path
    for path in file_dir:
        if os.path.isdir(os.path.join(from_path, path)):
            os.mkdir(os.path.join(to_path, path))
            copy_contents_to(os.path.join(from_path, path), os.path.join(to_path, path))
        elif os.path.isfile:
            shutil.copy(os.path.join(from_path, path), to_path)



if __name__ == "__main__":
    main()
