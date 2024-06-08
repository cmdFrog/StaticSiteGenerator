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

    def to_html(self) -> str:
        html_string = ""
        if self.value == None:
            raise ValueError
        
        if self.tag == None:
            return str(self.value)
        
        if self.tag == "a":
            html_string = (f'<a{self.props_to_html()}>{self.value}</a>')

        if self.tag == "p":
            html_string = (f'<p>{self.value}</p>')

        
        return html_string
