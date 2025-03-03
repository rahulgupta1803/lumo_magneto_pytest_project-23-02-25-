import configparser

config = configparser.RawConfigParser()
fpath = "D://credence//pytest_projects//lumo_magneto_pytest_project(23-02-25)//configuration//config.ini"
config.read(fpath)

class ReadConfig():
    @staticmethod
    def get_email():
        email = config.get('common data','Email')
        return email

    @staticmethod
    def get_password():
        password = config.get('common data','Password')
        return password