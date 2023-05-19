import configparser

def getConfig():
    config = configparser.ConfigParser()
    config.read('C:\\Users\\Srk\\PycharmProjects\\PythonDemo\\Utilities\\properties.ini')
    return config
def getPass():
    return "ABC1155151"