import matplotlib.image as mpimg
import numpy as np


def load_image(name: str, upscale=True):
    try:
        img = mpimg.imread(name)
        return (img * 256).astype(int) if upscale else img
    except Exception:
        print("Cannot read {}".format(name))
        return None

def shuffle_in_unison(a, b):
    rng_state = np.random.get_state()
    np.random.shuffle(a)
    np.random.set_state(rng_state)
    np.random.shuffle(b)

