import re

def as_glob(query):
    glob = "*"
    for char in query:
        if char == " ":
            if glob[-1] != "*":
                glob += "*"
        else:
            glob += char
    glob = glob.rstrip("*") + "*"
    return glob
