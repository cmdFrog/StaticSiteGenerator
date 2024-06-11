
block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def markdown_to_blocks(markdown: str) -> list:
    final_list = []
    split = markdown.split('\n\n')
    for string in split:
        if string:
            final_list.append(string.strip(" "))
    return final_list

def block_to_block_type(block: str) -> str:
    split = block.split("\n")
    if (block.startswith("# ")
        or block.startswith("## ")
        or block.startswith("### ")
        or block.startswith("#### ")
        or block.startswith("##### ")
        or block.startswith("###### ")
        ):
        return block_type_heading
    if len(split) > 1 and split[0].startswith("```") and split[-1].startswith("```"):
        return block_type_code
    if block.startswith(">"):
        for line in split:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    if any(line.strip().startswith("* ") or line.strip().startswith("- ") for line in split):
        return block_type_unordered_list
    if block.startswith("- "):
        for line in split:
            if not line.startswith("- "):
                return block_type_paragraph
        return block_type_unordered_list
    if block.startswith("1. "):
        i = 1
        for line in split:
            if not line.startswith(f"{i}. "):
                return block_type_paragraph
            i += 1
        return block_type_ordered_list
    return block_type_paragraph
