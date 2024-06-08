class HTMLNode:
    def __init__(self, tag =None, value =None, children =None, props =None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):    # Child classes will override this method to render themselves to HTML
        raise NotImplementedError
    
    def props_to_html(self) -> str:    # Take props dict and construct string that represents the HTML
        html_string = ""
        keys = self.props.keys()
        for key in keys:
            html_string = html_string + (f' {key}="{self.props[key]}"')
        return html_string
    
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:  # Maybe change this later to handle similar tags in one if statement with <self.tag>...</self.tag>
        html_string = ""
        if self.value == None:
            raise ValueError("Value not found")
        
        if self.tag == None:
            return str(self.value)
        
        if self.tag == "a":  # Links
            html_string = (f'<a{self.props_to_html()}>{self.value}</a>')

        if self.tag == "p":  # Paragraphs
            html_string = (f'<p>{self.value}</p>')

        if self.tag == "b":  # Bold
            html_string = (f'<b>{self.value}</b>')

        if self.tag == "i":
            html_string = (f'<i>{self.value}</i>')

        
        return html_string
    
class ParentNode(HTMLNode):
    def __init__(self, children, tag=None, props=None) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self):
        html_string = ""
        temp_string = ""
        if self.tag == None:
            raise ValueError("Tag not found.")
        
        if self.children == None or self.children == []:
            raise ValueError("No children found.")
        
        for i in range(0, len(self.children)):
            temp_string = temp_string + f'{self.children[i].to_html()}'
        
        html_string = f'<{self.tag}>{temp_string}</{self.tag}>'
        
        return html_string
        
