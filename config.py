import configparser

FILE = "config.ini"

config = configparser.ConfigParser()
config.read(FILE)
config.sections()

HASH_KEY = config['CONFIG']['HASH_KEY']
ACCOUNT_SID = config['CONFIG']['ACCOUNT_SID']
AUTH_TOKEN = config['CONFIG']['AUTH_TOKEN']

NUMBER = config['CONFIG']['NUMBER']
SENDER = config['CONFIG']['SENDER']
TEAM = config['CONFIG']['TEAM']
USERNAME = config['CONFIG']['USERNAME']