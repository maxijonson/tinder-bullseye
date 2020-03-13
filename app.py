from utils import get_recs, get_teasers, get_image, compare, rescale, like, dislike, superlike
from colorama import init, deinit, Fore, Style
from constants import KEY_LIKE, KEY_PASS, KEY_SUPERLIKE
import cv2

# Init Colorama
init()

recs = get_recs()
teasers = get_teasers()

teaser_images = {teaser['user']['_id']: get_image(
    teaser['user']['photos'][0]['url']) for teaser in teasers}

for rec in recs:
    user = rec['user']
    rec_id = user['_id']
    print(f"{Fore.GREEN}Analyzing {user['name']} ({rec_id}) ...")

    for rec_photo in user['photos']:
        print(f"\t{Fore.BLUE}Image {rec_photo['url']}")
        rec_img = get_image(rec_photo['url'])

        for (tea_id, tea_img) in teaser_images.items():
            print(
                f"\t\t{Fore.BLACK}{Style.BRIGHT}Comparing with teaser {tea_id}")
            if (compare(rec_img, tea_img)):
                for i, rec_found_img in enumerate([get_image(pic['url']) for pic in user['photos']]):
                    cv2.imshow(f"Rec {i}", rescale(rec_found_img, 30))
                cv2.imshow("Teaser", rescale(tea_img, 30))
                action = cv2.waitKey(0)
                cv2.destroyAllWindows()
                if (action == KEY_LIKE or action == KEY_LIKE - 32):
                    like(rec_id)
                if (action == KEY_PASS or action == KEY_PASS - 32):
                    dislike(rec_id)
                if (action == KEY_SUPERLIKE or action == KEY_SUPERLIKE - 32):
                    superlike(rec_id)
    print("\n")

# Deinit Colorama
deinit()
