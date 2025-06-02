from pathlib import Path
import os
import shutil

from textnode import TextNode, TextType
# helpers
def reset_public_dir():
    public_dir = Path("./../public")
    print(f"Resetting public directory: {os.listdir(public_dir)}")
    if public_dir.exists():
        shutil.rmtree(public_dir)

def main():
    new_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(new_node)
    reset_public_dir()

main()