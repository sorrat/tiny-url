from os.path import dirname, abspath, join


ROOT_DIR = dirname(dirname(abspath(__file__)))
DB_PATH = join(ROOT_DIR, 'tiny_url.ldb')


import sys
sys.path.insert(0, ROOT_DIR)
