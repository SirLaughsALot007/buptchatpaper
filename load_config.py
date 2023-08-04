import os
import configparser

def load_config():
    try:
        CONFIG_PATH = os.environ['CONFIG_PATH']
    except KeyError:
        raise KeyError("Please set the environment variable CONFIG_PATH to the path of the config file.")

    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)
    return config