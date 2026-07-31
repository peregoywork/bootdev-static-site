from textnode import TextNode
from build_public import build_public_from_static, generate_page
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    build_public_from_static()
    generate_page('content/index.md', 'template.html', 'public/index.html')

if __name__=='__main__':
    main()


