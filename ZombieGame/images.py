from pygame import image, transform
from os import listdir, path

from constants import BACKGROUND_IMAGE_PATH, PLAYER_IMAGES_PATH, \
    MALE_ZOMBIE_IMAGES_PATH, DISPLAY_SIZE


def get_images(main_path):
    """
    Iterates through the subdirectories of the character main image directory
    saving their names as the character state, in each iteration, first, it
    loads the original set of images, rescales them to 40% of its original
    size and saves them as a tuple in a dict with the key 'RIGHT', then it
    flips horizontally the images, updates the dict with the flipped images
    in a tuple with the key 'LEFT', and finally it saves the dict in another
    dict with the current state as an all caps string as key.

    :param main_path: path to the character image directory
    :return: {'STATE': {
                'RIGHT': [right_images],
                'LEFT': [left_images]
            }}
    """

    # gets a list of subdirectories of main path as a state list
    states = listdir(main_path)
    image_set = {}  # to be populated with
    # 'STATE': {'RIGHT': [right_images], 'LEFT': [left_images]}

    for state in states:
        state_path = path.join(main_path, state)

        # creates a list of paths to the images files within the state path,
        # sorted by the numeric values in the file's name.
        images_paths = [
            path.join(state_path, file) for file in sorted(
                listdir(state_path),
                key=lambda p: int(''.join([x for x in p[:] if x.isnumeric()])))
        ]

        images = []  # to be populated with image objects

        for img_path in images_paths:
            img = image.load(img_path)  # loads image from path

            # gets image dimensions
            img_height = img.get_height()
            img_width = img.get_width()

            # rescales the image to 40% of its original size
            img_scale = (
                int(img_width * 0.4),
                int(img_height * 0.4)
            )

            img = transform.scale(img, img_scale)  # applies the scaling

            images.append(img)

        # redeclares images as a dictionary with its orientation as key and a
        # tuple containing the images objects as value
        images = {
            'RIGHT': tuple(images)
        }

        # updates images dictionary with a new key for the left orientation
        # and a tuple containing the original images horizontally mirrored
        images.update({
            'LEFT': tuple(transform.flip(
                img, True, False) for img in images['RIGHT']
                )
        })

        # updates the image set with the current state as all capitalized
        # string as key and the current images dictionary as value
        image_set.update({state.upper(): images})

    return image_set


# gets background image and rescales it to the display size
BACKGROUND_IMAGE = transform.scale(
    image.load(BACKGROUND_IMAGE_PATH), DISPLAY_SIZE
)

# gets images from ninja images file
PLAYER_IMAGES = get_images(PLAYER_IMAGES_PATH)

# gets images from male zombie image file
MALE_ZOMBIE_IMAGES = get_images(MALE_ZOMBIE_IMAGES_PATH)

