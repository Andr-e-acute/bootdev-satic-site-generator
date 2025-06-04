from pathlib import Path
import os
import sys
import shutil
from markdown_utils import extract_title
from html_converter import markdown_to_html_node
from htmlnode import  HTMLNode
from textnode import TextNode, TextType
basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
print(f"Base path is set to: {basepath}")
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

    title = extract_title(markdown)
 
    html_output = (
        template
        .replace("{{ Title }}", title)
        .replace("{{ Content }}", html)
        .replace("href=\"/", f"href=\"{basepath}")
        .replace("src=\"/", f"src=\"{basepath}")
    )
# write the output to the destination path
    destPath= Path(destPath)
    if not destPath.parent.exists():
        os.makedirs(destPath.parent)
    destPath.write_text(html_output, encoding='utf-8')
def generate_pages_recursively(dir_path_content,template_path,dest_dir_path):
    for item in os.listdir(dir_path_content):
        if item.endswith(".md"):
            content_path = os.path.join(dir_path_content, item)
            relative_path = os.path.relpath(content_path, dir_path_content)
            dest_path = os.path.join(dest_dir_path, relative_path.replace(".md", ".html"))
            generate_page(content_path, template_path, dest_path)
        elif os.path.isdir(os.path.join(dir_path_content, item)):
            sub_dir_content = os.path.join(dir_path_content, item)
            sub_dir_dest = os.path.join(dest_dir_path, item)
            if not os.path.exists(sub_dir_dest):
                os.makedirs(sub_dir_dest)
            generate_pages_recursively(sub_dir_content, template_path, sub_dir_dest)
def main():
    reset_public_dir("./docs")
    populate_public_dir("./static", "./docs")
    generate_pages_recursively(f"./content", f"./template.html", f"./docs")

main()