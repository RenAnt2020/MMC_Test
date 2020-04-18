import configparser
import os

Config_path = os.path.dirname(__file__) + '/../conf/config.ini'
config = configparser.ConfigParser()
config.read(Config_path, encoding='utf-8')
Env = 'dev'
def url():
    return config.get(Env,'url')
def username():
    return config.get(Env,'username')
def password():
    return config.get(Env,"password")



if __name__ == '__main__':

    print(url())