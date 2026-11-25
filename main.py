#!/usr/bin/env python3
"""Write the day's news poster to /output/entry.png.

The image is committed in this repository as entry.png; this program only
copies its bytes, so two runs are byte-identical and no network is used.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("ENTRY_OUT", "/output/entry.png")


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "entry.png"), OUT)


if __name__ == "__main__":
    main()
