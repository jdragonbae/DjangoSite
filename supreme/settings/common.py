import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_DIR = os.path.join(BASE_DIR, '../.config')
CONFIG_SECRET_COMMON_FILE = os.path.join(CONFIG_DIR, 'common.json')
CONFIG_SECRET_DEBUG_FILE = os.path.join(CONFIG_DIR, 'dev.json')
CONFIG_SECRET_DEPLOY_FILE = os.path.join(CONFIG_DIR, 'prod.json')
config_secret_common = json.loads(open(CONFIG_SECRET_COMMON_FILE).read())

SECRET_KEY = config_secret_common['django']['SECRET_KEY']
