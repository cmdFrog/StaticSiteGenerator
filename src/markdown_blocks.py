


def markdown_to_blocks(markdown: str) -> list:
    final_list = []
    split = markdown.split('\n\n')
    for string in split:
        if string:
            final_list.append(string)
    return final_list
