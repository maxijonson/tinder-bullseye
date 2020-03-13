from os.path import join, dirname
from secret import X_AUTH_TOKEN

PROJECT = dirname(__file__)

# Endpoint base
API = "https://api.gotinder.com"

# Endpoints
# GET
RECS = f"{API}/v2/recs/core"
TEASERS = f"{API}/v2/fast-match/teasers"
LIKE = f"{API}/like"
PASS = f"{API}/pass"
COUNT = f"{API}/v2/fast-match/count"
#POST
SUPERLIKE = lambda id: f"{API}/like/{id}/super"

# Data files
DATA_FOLDER = join(PROJECT, "data")
DATA_RECS = join(DATA_FOLDER, "recs.json")
DATA_TEASERS = join(DATA_FOLDER, "teasers.json")

# Image extension
IMG_EXT = "jpeg"

# Error margins
MARGIN_WIDTH = 50
MARGIN_HEIGHT = 50
MARGIN_DIFF = 1000

# Image max dimensions
IMG_MAX_W = 320
IMG_MAX_H = 480

# Keys
KEY_LIKE = 108 # l
KEY_PASS = 112 # p
KEY_SUPERLIKE = 115 # s


# Request Headers
HEADERS = {'x-auth-token': X_AUTH_TOKEN, 'User-Agent': 'TinderBullseye/1.0.0'}
