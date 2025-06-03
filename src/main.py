from pathlib import Path
import os
import shutil
from markdown_utils import extract_title
from html_converter import markdown_to_html_node
from htmlnode import  HTMLNode
from textnode import TextNode, TextType
# helpers
def reset_public_dir(path):
    public_dir = Path(path)
    if public_dir.exists():

        shutil.rmtree(public_dir)
    os.mkdir(public_dir)
def populate_public_dir(fromPath,toCopyPath):
    if not os.path.exists(fromPath):
        raise FileNotFoundError(f"Source path does not exist: {fromPath}")
    if not os.path.exists(toCopyPath):
        raise FileNotFoundError(f"Destination path does not exist: {toCopyPath}")
    source_dir = os.listdir(fromPath)
    for item in source_dir:
        if(os.path.isfile(fromPath + "/" + item)):

           shutil.copy(fromPath + "/" + item, toCopyPath)
        elif(os.path.isdir(fromPath + "/" + item)):

              os.mkdir(toCopyPath + "/" + item)
              populate_public_dir(fromPath + "/" + item, toCopyPath + "/" + item)
def generate_page(fromPath, templatePath, destPath):
    print(f"Generating page from {fromPath} using template {templatePath} to {destPath}")
    markdown_file= open(fromPath, 'r')
    markdown = markdown_file.read()
    markdown_file.close()
    template_file = open(templatePath, 'r')
    template = template_file.read()
    template_file.close()
    html= markdown_to_html_node(markdown).to_html()
    print (f"'HTML generated: {html}'")	
    title = extract_title(markdown)
def main():
    new_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")

    reset_public_dir("./public")
    populate_public_dir("./static", "./public")

main()