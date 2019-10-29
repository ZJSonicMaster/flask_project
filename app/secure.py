DEBUG = True
HOST = '0.0.0.0'

# URI连接包括：mysql+(mysql驱动)://(用户名):(密码)@(数据库IP):(端口)/(数据库名)
# SQLAlchemy支持分布式数据库
SQLALCHEMY_DATEBASE_URI = 'mysql+cymysql://root:root@localhost:3306/fisher'