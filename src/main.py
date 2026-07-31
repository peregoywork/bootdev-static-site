from textnode import TextNode
from build_public import clean_directory, copy_directory, generate_page
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BASE_PATH = Path(__file__).resolve().parent.parent
STATIC_DIR = BASE_PATH / "static"
PUBLIC_DIR = BASE_PATH / "public" 


def build_public_from_static():
    clean_directory(PUBLIC_DIR)
    copy_directory(STATIC_DIR, PUBLIC_DIR)


def main():
    build_public_from_static()
    generate_page('content/index.md', 'template.html', 'public/index.html')


if __name__=='__main__':
    main()


