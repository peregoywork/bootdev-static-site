import logging
import shutil
from pathlib import Path
from markdown_blocks import markdown_to_html_node
from extract_markdown import extract_title

logger = logging.getLogger(__name__)



# read from ../static
# clean ../public
# recursively copy all contents to ..public

BASE_PATH = Path(__file__).resolve().parent.parent
STATIC_DIR = BASE_PATH / "static"
PUBLIC_DIR = BASE_PATH / "public" 

if not STATIC_DIR.exists():
    STATIC_DIR.mkdir(parents=True, exist_ok=True)



def clean_directory(dir_path: Path):
    logger.info(f"deleting and recreating empty dir {dir_path}")
    shutil.rmtree(dir_path.resolve())
    dir_path.mkdir(parents=True, exist_ok=True)


def copy_directory(src: Path, dest: Path):
    logger.info(f"copying files from {src} to {dest}")
    for item in src.iterdir():
        if item.is_dir():
            (dest / item.name).mkdir()
            copy_directory((src / item.name), (dest / item.name))
        if item.is_file():
            shutil.copy((src / item.name), (dest / item.name))


def generate_page(from_path, template_path, dest_path):
    logger.info(f"Generating page from {from_path} to {dest_path} using {template_path}")
    src_content = None
    template = None
    
    with open(from_path, 'r') as f:
        src_content = f.read()
    with open(template_path, 'r') as f:
        template = f.read()

    html_node = markdown_to_html_node(src_content).to_html()
    title = extract_title(src_content)

    template = template.replace('{{ Title }}', title)
    template = template.replace('{{ Content }}', html_node)

    dest_path = dest_path.with_suffix(".html")
    if not dest_path.exists():
        logger.info(f"file does not exist. Touch")
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        dest_path.touch()
    with open(dest_path, 'w') as f:
       f.write(template)
    
    
def generate_pages_recursive(src_dir_path, template_path, dest_dir_path):
    logger.info("begin recusive generation")
    for item in src_dir_path.iterdir():
        src = src_dir_path / item.name
        dest = dest_dir_path / item.name
        if item.is_dir():
            generate_pages_recursive(src, template_path, dest)
        elif item.is_file():
            generate_page(src, template_path, dest)


