class  Config():
    Debug = False
    Test = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRECT_KEY = '110'
    SESSION_TYPE = 'redis'

    MAIL_SERVER = 'smtp.qq.com'
    MAIL_USERNAME = '812324872@qq.com'
    MAIL_PASSWORD = 'migpwqgexfbabbeb'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False

def get_database_uri(DATABASE):
    dialect = DATABASE.get('dialect')
    driver = DATABASE.get('driver')
    username = DATABASE.get('username')
    password = DATABASE.get('password')
    host = DATABASE.get('host')
    port = DATABASE.get('port')
    database = DATABASE.get('database')
    print('{}+{}://{}:{}@{}:{}/{}'.format(dialect, driver, username, password, host, port, database))
    return '{}+{}://{}:{}@{}:{}/{}'.format(dialect, driver, username, password, host, port, database)

class DevelopConfig(Config):
    DATABASE = {
        'dialect': 'mysql',
        'driver': 'pymysql',
        'username': 'root',
        'password': '123456',
        'host': 'localhost',
        'port': '3306',
        'database': 'fruit'
    }
    SQLALCHEMY_DATABASE_URI = get_database_uri(DATABASE)

ENV_NAME = {
    'develop':DevelopConfig
}