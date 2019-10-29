from sqlalchemy import Column, Integer, String

# sqlalchemy
# Flask_SQLAlchemy 操作数据库
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    id = Column(Integer, primary_key = True, nullable = False, autoincrement = True)
    title = Column(String(50), nullable = False)
    author = Column(String(30), default = '未名')
    binding = Column(String(50))
    # 出版社
    publisher = Column(String(30))
    price = Column(String(20))
    pages = Column(Integer)
    # 发布时间
    pubdate = Column(String(20))
    isbn = Column(String(15), nullable = False, unique = True)
    # 简介
    summary = Column(String(50))
    image = Column(String(50))