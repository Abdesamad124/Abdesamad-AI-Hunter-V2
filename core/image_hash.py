import hashlib


class ImageHash:

    @staticmethod
    def generate(image_path):

        with open(image_path, "rb") as f:

            return hashlib.md5(

                f.read()

            ).hexdigest()