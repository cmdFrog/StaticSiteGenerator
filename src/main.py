from page_gen import copy_contents_to, generate_pages_recursive

def main():
    print("Main Started")
    copy_contents_to("/home/cmdfrog/workspace/github.com/cmdFrog/SSG/static", "/home/cmdfrog/workspace/github.com/cmdFrog/SSG/public")
    generate_pages_recursive("content/", "template.html", "public/")


if __name__ == "__main__":
    main()
