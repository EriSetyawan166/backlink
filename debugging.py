import os
import hashlib

BASE_PATH = os.getcwd()


def dump_html(html_text: str):
    path = BASE_PATH

    string_file = str(123)
    print(string_file)
    file_name = hashlib.sha256(string_file.encode("utf-8")).hexdigest()

    file_extension = ".html"

    file = path + file_name + file_extension

    with open(file, "wb") as f:
        f.write(html_text.encode("utf-8"))

    return file
