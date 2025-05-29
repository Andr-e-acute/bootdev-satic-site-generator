class HTMLNode:
    def __init__(self, tag=None,value=None, children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError("This method should be implemented in subclasses")
    def props_to_html(self):
        propreturn = ""
        if self.props is None:
            return propreturn
        for key, value in self.props.items():
             propreturn += f" {key}=\"{value}\""
        return propreturn
    def __repr__(self):
        return f"HTMLNODE({self.tag}, {self.value}, {self.children}, {self.props})"
    