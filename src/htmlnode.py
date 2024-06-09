class HTMLNode:
    def __init__(self,
        tag: str = None,
        value: str = None,
        children: list = None,
        props: dict = None,
    ) -> None:

        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(
        self,
    ):  # Child classes will override this method to render themselves to HTML
        raise NotImplementedError

    def props_to_html(
        self,
    ) -> str:  # Take props dict and construct string that represents the HTML
        html_string = ""
        keys = self.props.keys()
        for key in keys:
            html_string = html_string + (f' {key}="{self.props[key]}"')
        return html_string

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, value: str, tag: str = None, props: dict = None) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:  # Maybe change this later to handle similar tags in one if statement with <self.tag>...</self.tag>
        html_string = ""
        if self.value is None:
            raise ValueError("Value not found")

        if self.tag is None: # Raw Text
            return str(self.value)

        if self.tag == "a":    # Links
            html_string = f"<a{self.props_to_html()}>{self.value}</a>"

        if self.tag == "p":    # Paragraphs
            html_string = f"<p>{self.value}</p>"

        if self.tag == "b":    # Bold
            html_string = f"<b>{self.value}</b>"

        if self.tag == "i":    # Italics
            html_string = f"<i>{self.value}</i>"

        if self.tag == "img":  # Image
            html_string = f'<img{self.props_to_html()}>'

        if self.tag == "code": # Code
            html_string = f'<code>{self.value}</code>'

        return html_string


class ParentNode(HTMLNode):
    def __init__(self, children: list, tag: str = None, props: dict = None) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        html_string = ""
        temp_string = ""
        if self.tag is None:
            raise ValueError("Tag not found.")

        if self.children is None or self.children == []:
            raise ValueError("No children found.")

        for child in self.children:
            temp_string = temp_string + f"{child.to_html()}"

        html_string = f"<{self.tag}>{temp_string}</{self.tag}>"

        return html_string
