import logging
import shutil
from pathlib import Path

logger = logging.getLogger(__name__)



# read from ../static
# clean ../public
# recursively copy all contents to ..public

BASE_PATH = Path(__file__).resolve().parent.parent
STATIC_DIR = BASE_PATH / "static"
PUBLIC_DIR = BASE_PATH / "public" 

if not STATIC_DIR.exists():
    STATIC_DIR.mkdir(parents=True, exist_ok=True)
 

def clean_directory(dir: Path):
    shutil.rmtree(dir.resolve())
    PUBLIC_DIR.mkdir(parents=True, exist_ok=True)

def copy_directory(src: Path, dest: Path):
    logger.info(src)
    logger.info(dest)
    for item in src.iterdir():
        if item.is_dir():
            (dest / item.name).mkdir()
            copy_directory((src / item.name), (dest / item.name))
        if item.is_file():
            shutil.copy((src / item.name), (dest / item.name))

def build_public_from_static():
    clean_directory(PUBLIC_DIR)
    copy_directory(STATIC_DIR, PUBLIC_DIR)

