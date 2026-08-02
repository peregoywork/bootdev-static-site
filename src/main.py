from textnode import TextNode
from build_public import (
    clean_directory, 
    copy_directory, 
    generate_pages_recursive, 
    ensure_exists
)
from pathlib import Path
import sys
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


BASE_PATH = Path(__file__).resolve().parent.parent
STATIC_DIR = BASE_PATH / "static"
DOCS_DIR = BASE_PATH / "docs"
CONTENT_DIR = BASE_PATH / "content"


def get_basepath():
    args = sys.argv
    if len(args) > 1:
        return args[1]
    return '/'


def main():
    basepath = get_basepath()

    print(basepath)

    ensure_exists([STATIC_DIR, DOCS_DIR, CONTENT_DIR])    
    clean_directory(DOCS_DIR)
    copy_directory(STATIC_DIR, DOCS_DIR)
    generate_pages_recursive(CONTENT_DIR, 'template.html', DOCS_DIR, basepath)


if __name__=='__main__':
    main()


