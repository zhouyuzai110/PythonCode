import os
from docx import Document
from urllib.parse import quote_plus as urlquote
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, UniqueConstraint, Index, VARCHAR
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.mysql import LONGTEXT

# 文章标题
# 文章一级标题
# 文章二级标题
# 文章署名
# 文章副标题
# 黑体小标题

Base = declarative_base()
basedir = 'C:/Users/saber/Desktop/pythonscript/xxck'
# article_list = []
file_name = "学习参考第9辑-纪实、周年、综述.docx"
password = 'qwe123!@#'
pwd = urlquote(password)
engine = create_engine("mysql+pymysql://flaskapi:{}@192.168.1.5:3306/flaskapi?charset=utf8mb4".format(pwd))
Session = sessionmaker(bind=engine)


class Xxck(Base):
    __tablename__ = 'xxck'

    id = Column(Integer, primary_key=True)
    filename = Column(VARCHAR(200))
    articlename = Column(VARCHAR(200))
    content = Column(LONGTEXT, nullable=True)


def init_db():
    """
    根据类创建数据库表
    :return: 
    """
    engine = create_engine(
        "mysql+pymysql://flaskapi:{}@192.168.1.5:3306/flaskapi?charset=utf8mb4".format(pwd),
        max_overflow=0,  # 超过连接池大小外最多创建的连接
        pool_size=5,  # 连接池大小
        pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
        pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
    )

    Base.metadata.create_all(engine)


def drop_db():
    """
    根据类删除数据库表
    :return: 
    """
    engine = create_engine(
        "mysql+pymysql://flaskapi:{}@192.168.1.5:3306/flaskapi?charset=utf8mb4".format(pwd),
        max_overflow=0,  # 超过连接池大小外最多创建的连接
        pool_size=5,  # 连接池大小
        pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
        pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
    )

    Base.metadata.drop_all(engine)


def file_list(dir):
    return [os.path.join(dir, fn) for fn in os.listdir(dir)]


def create_word_paragraph_text(file_name):
    paragraph_list = []
    document = Document(file_name)
    paragraphs = document.paragraphs
    for paragraph in paragraphs:
        if paragraph.style.name == "文章标题":
            paragraph_list.append("split" + paragraph.text)
        else:
            paragraph_list.append(paragraph.text)
    paragraph_text = 'fffff'.join(paragraph_list)
    return paragraph_text


def insert_article_list(filename, paragraph_text):
    articles = paragraph_text.split("split")
    for article in articles:
        # print(article)
        insert_article(filename, article)


def insert_article(filename, content):
    session = Session()
    content_list = content.split("fffff")
    if len(content_list[0]) > 1:
        obj = Xxck(filename=filename, articlename=content_list[0], content='\n'.join(content_list[1:]))
        session.add(obj)
    # 提交事务
    session.commit()
    # 关闭session
    session.close()


def main():
    for file in file_list(basedir):
        filename = file.replace('.docx', '').replace('C:/Users/saber/Desktop/pythonscript/xxck\\', '')
        paragraph_text = create_word_paragraph_text(file)
        print(filename, paragraph_text)
        insert_article_list(filename, paragraph_text)


if __name__ == '__main__':
    main()
    # drop_db()
    # init_db()