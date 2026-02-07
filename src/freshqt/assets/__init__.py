"""

    freshqt  -  A modern, refreshed take on PyQt user interfaces

    This file is a part of the freshqt
    project and distributed under MIT license.
    https://github.com/kadir014/freshqt

"""

from importlib.resources import files
from pathlib import Path


def _collect_heroicons() -> dict[str, Path]:
    icons = {}
    base = files(__name__)

    for file in base.iterdir():
        p = Path(file)
        if p.suffix == ".svg" and p.is_file():
            icons[p.stem.replace("hi-", "")] = p

    return icons

def _collect_images() -> dict[str, Path]:
    images = {}
    base = files(__name__)

    for file in base.iterdir():
        p = Path(file)
        if p.suffix == ".png" and p.is_file():
            images[p.stem] = p

    return images


HEROICONS = _collect_heroicons()

IMAGES = _collect_images()


__all__ = ("HEROICONS", "IMAGES")