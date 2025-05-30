from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        if tag is None:
            raise ValueError("All parent nodes must have a tag.")    
        if children is None:
            raise ValueError("All parent nodes must have children.")
        super().__init__(tag=tag, children=children, props=props)
    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag to convert to HTML.")
        if self.children is None:
            raise ValueError("ParentNode must have children to convert to HTML.")
        html= ""
        for child in self.children:
            html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{html}</{self.tag}>"