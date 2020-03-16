import os

import numpy as np
import matplotlib.image as mpimg


def shuffle_in_unison(a, b):
    rng_state = np.random.get_state()
    np.random.shuffle(a)
    np.random.set_state(rng_state)
    np.random.shuffle(b)


def load_image(name: str):
    try:
        img = mpimg.imread(name)
        return (img * 256).astype(int)
    except Exception:
        print("Cannot read {}".format(name))
        return None


def get_all_files(dir_name):
    for dirpath, _, names in os.walk(dir_name):
        for name in names:
            yield os.path.join(dirpath, name)


def get_duplicates(names, images):
    for name in names:
        current = load_image(name)
        if any(np.array_equal(current, image) for image in images):
            yield name


def remove_test_duplicates():
    for label in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]:
        test_path = os.path.join("../blobs/notMNIST_small/", label)
        test_images = [load_image(f) for f in get_all_files(test_path)]
        train_path = os.path.join("../blobs/notMNIST_large/", label)
        train_files = get_all_files(train_path)
        for d in get_duplicates(train_files, test_images):
            print("Removing {}".format(d))
            os.remove(d)
        print("Finished with {}".format(label))


if __name__ == "__main__":
    remove_test_duplicates()
