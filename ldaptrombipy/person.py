import os
import glob

from env import STATIC_IMAGE_PATH


class Person:
    def __init__(self, data) -> None:
        self.name = data.get("name", None)
        self.groups = data.get("groups", [])
        self.picture = self.find_picture()

    def find_picture(self):
        os.chdir(str(STATIC_IMAGE_PATH))
        p = None
        for file in glob.glob(f"{self.name}.*"):
            p = file
        return p
