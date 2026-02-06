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


HEROICONS = _collect_heroicons()


__all__ = ("HEROICONS",)