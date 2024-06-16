from page_gen import copy_contents_to, generate_page

def main():
    print("Main Started")
    copy_contents_to("/home/cmdfrog/workspace/github.com/cmdFrog/SSG/static", "/home/cmdfrog/workspace/github.com/cmdFrog/SSG/public")
    generate_page("content/index.md", "template.html", "public/index.html")


if __name__ == "__main__":
    main()
