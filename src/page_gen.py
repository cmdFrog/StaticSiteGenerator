import os
import shutil
from markdown import markdown_to_blocks

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

markdown_doc = """# Header 1

## Header 2

This is a paragraph with some **BOLD** and *ITALIC* in it.

> Quote from Obama

```
CHECK OUT MY COOL CODE! IT HAS AN IMAGE IN IT ![alt text for image](url/of/image.jpg)
```

1. I like cheese
2. you like cheese
3. we like cheese
4. uhh cheese

* this is a list
* still a list
"""

print(extract_title(markdown_doc))
