import tomllib
import os


def load_toml(filepath):
    if not os.path.exists(filepath):
        return None

    with open(filepath, 'r') as f:
        return tomllib.load(f.read())
