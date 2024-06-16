import os
import shutil
from markdown import markdown_to_blocks, markdown_to_html_node

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

def extract_title(markdown: str) -> str:
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block.startswith("# "):
            return block.split("# ")[1]

    raise ValueError("No header found")

def read_file(path):
    file = open(path, encoding="utf-8")
    try:
        file_contents = file.read()
    except Exception as e:
        raise ValueError(f"Failed to read the file {e}") from e
    finally:
        file.close()
    return file_contents

def relative_to_absolute(relative_path):
    if os.path.isabs(relative_path):
        return relative_path
    if "SSG" in relative_path.split(os.path.sep):
        raise SyntaxError("If given path is relative, it must be relative to inside the SSG directory. ie: content/index.md and not SSG/content/index.md")
    src_directory = os.path.dirname(os.path.realpath(__file__))
    ssg_directory = os.path.abspath(os.path.join(src_directory, ".."))
    return os.path.join(ssg_directory, relative_path)



def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    from_path = relative_to_absolute(from_path)
    template_path = relative_to_absolute(template_path)
    dest_path = relative_to_absolute(dest_path)
    markdown_file = read_file(from_path)
    html_template = read_file(template_path)
    html_node = markdown_to_html_node(markdown_file)
    html_cont = html_node.to_html()
    title = extract_title(markdown_file)
    content_replace = html_template.replace("{{ Content }}", html_cont)
    final_html = content_replace.replace("{{ Title }}", title)
    dest_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    with open(dest_path, "w", encoding="utf-8") as file:
        file.write(final_html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    abs_path_content = relative_to_absolute(dir_path_content)
    abs_path_dest = relative_to_absolute(dest_dir_path)
    file_dir = os.listdir(abs_path_content)
    for item in file_dir:
        abs_path_item = os.path.join(abs_path_content, item)
        if os.path.isdir(abs_path_item):
            dest_subdir = os.path.join(abs_path_dest, item)
            os.mkdir(dest_subdir)
            generate_pages_recursive(abs_path_item, template_path, dest_subdir)
        elif os.path.isfile(abs_path_item) and item.endswith('.md'):
            dest_file_path = os.path.join(abs_path_dest, os.path.splitext(item)[0] + '.html')
            generate_page(abs_path_item, template_path, dest_file_path)



#generate_page("/home/cmdfrog/workspace/github.com/cmdFrog/SSG/content/index.md", "/home/cmdfrog/workspace/github.com/cmdFrog/SSG/template.html", "/home/cmdfrog/workspace/github.com/cmdFrog/SSG/public/index.html")
