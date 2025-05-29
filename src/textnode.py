from enum import Enum
class TextType(Enum):
    TEXT = "text"           # plain, unformatted text
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text,text_type, url):
        self.text_type = text_type
        self.url = url 
        self.text = text

    def __eq__(self, other):
        return(
        self.text_type == other.text_type and
        self.url == other.url and
        self.text == other.text
    )
    def __repr__(self):
       return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


