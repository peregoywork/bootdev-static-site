from textnode import TextNode
from build_public import clean_directory, copy_directory, generate_pages_recursive
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BASE_PATH = Path(__file__).resolve().parent.parent
STATIC_DIR = BASE_PATH / "static"
PUBLIC_DIR = BASE_PATH / "public" 
CONTENT_DIR = BASE_PATH / "content"


def main():
    clean_directory(PUBLIC_DIR)
    copy_directory(STATIC_DIR, PUBLIC_DIR)
    generate_pages_recursive(CONTENT_DIR, 'template.html', PUBLIC_DIR)


if __name__=='__main__':
    main()


