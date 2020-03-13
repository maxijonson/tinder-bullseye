import os
import requests
import json
from skimage import io
import cv2
from constants import RECS, TEASERS, LIKE, PASS, COUNT, DATA_RECS, DATA_TEASERS, HEADERS, IMG_EXT, MARGIN_HEIGHT, MARGIN_WIDTH, MARGIN_DIFF, IMG_MAX_H, IMG_MAX_W, LIKE, PASS, SUPERLIKE


def createAndOpen(filename, mode):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    return open(filename, mode)


def get_recs():
    with createAndOpen(DATA_RECS, 'w') as f:
        recs = requests.get(RECS, headers=HEADERS).json()[
            "data"]["results"]
        json.dump(recs, f)
    return recs


def get_teasers():
    with createAndOpen(DATA_TEASERS, 'w') as f:
        teasers = requests.get(TEASERS, headers=HEADERS).json()[
            "data"]["results"]
        json.dump(teasers, f)
    return teasers


def get_image(url):
    image = io.imread(url)
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


def compare(original, other):
    og_w, og_h, og_c = original.shape
    ot_w, ot_h, ot_c = other.shape

    # Same size
    if og_w == ot_w and og_h == ot_h:

        difference = cv2.subtract(original, other)
        b, g, r = cv2.split(difference)
        nonZeroes = sum([cv2.countNonZero(p) for p in cv2.split(difference)])

        if (nonZeroes < MARGIN_DIFF):
            return True

    return False


def rescale(img, scale):
    if img.shape[0] >= IMG_MAX_H:
        h = IMG_MAX_H
        w = int((h / img.shape[0]) * img.shape[1])
    elif img.shape[1] >= IMG_MAX_W:
        w = IMG_MAX_W
        h = int((w / img.shape[1]) * img.shape[0])
    else:
        w = int(img.shape[1])
        h = int(img.shape[0])
    return cv2.resize(img, (w, h))


def like(id):
    return requests.get(f"{LIKE}/{id}")


def dislike(id):
    return requests.get(f"{PASS}/{id}")


def superlike(id):
    return requests.post(SUPERLIKE(id))
