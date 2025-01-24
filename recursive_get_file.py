import os, time
import hashlib
from urllib.parse import quote_plus as urlquote

from sqlalchemy import (Column, Integer, String, Table, create_engine, insert, text, select, update, bindparam, delete)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engine = create_engine(f'mysql+pymysql://flaskapi:{urlquote("qwe123!@#")}@192.168.1.5:3306/flaskapi?charset=utf8mb4')

insert_list = []
update_list = []
hash_hit = []
local_book_path_list = []


class Base(DeclarativeBase):
    pass


class Library(Base):
    __tablename__ = "library"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    # book_name: Mapped[str] = mapped_column(String(200), unique=True)
    book_name: Mapped[str] = mapped_column(String(200))
    book_path: Mapped[str] = mapped_column(String(600), index=True)
    book_size: Mapped[str] = mapped_column(String(10))
    book_hash: Mapped[str] = mapped_column(String(100))


def timer_decorator(func):

    def wrapper(*args, **kwargs):
        begin_time = time.time()
        print('func {} timer begin'.format(func.__name__))
        result = func(*args, **kwargs)
        end_time = time.time()
        print('func {} timer end'.format(func.__name__))
        print("func {} used {:.2f}s".format(func.__name__, (end_time - begin_time)))
        return result

    return wrapper


@timer_decorator
def truncate_table():
    print("truncating table")
    with engine.connect() as conn:
        result = conn.execute(text("truncate table library"))
        conn.commit()
    print("truncated")


@timer_decorator
def drop_table():
    print("droping table")
    with engine.connect() as conn:
        result = conn.execute(text("drop table library"))
        conn.commit()
    print("droped")


@timer_decorator
def select_values(hash):

    # stmt = selec * from library WHERE book_hash = hash
    stmt = select(Library).where(Library.book_hash == hash)
    with engine.connect() as conn:
        for row in conn.execute(stmt):
            print(row)


@timer_decorator
def insert_values(insert_list):
    if len(insert_list) == 0:
        print('insert_list为空，退出')
        return
    # stmt = insert(Library).values(book_list)
    with engine.connect() as conn:
        result = conn.execute(
            insert(Library),
            insert_list,
        )
        conn.commit()


@timer_decorator
def update_values(update_list):
    if len(update_list) == 0:
        print('update_list为空，退出')
        return
    stmt = update(Library).where(Library.book_hash == bindparam("update_book_hash")).values(
        book_name=bindparam("update_book_name"), book_path=bindparam("update_book_path"))
    print(stmt)
    with engine.connect() as conn:
        conn.execute(
            stmt,
            update_list,
        )
        conn.commit()


@timer_decorator
def delete_values(delete_list):
    if len(delete_list) == 0:
        print('delete_list为空，退出')
        return
    for item in delete_list:
        stmt = delete(Library).where(Library.book_path == item)
        with engine.connect() as conn:
            conn.execute(stmt)
            conn.commit()


def get_db_book_list():
    stmt = select(Library.book_path, Library.book_hash)
    # print(stmt)
    with engine.connect() as conn:
        result = conn.execute(stmt)
        # print(result.all())
        path = []
        hash = []
        for res in result:
            path.append(res[0])
            hash.append(res[1])
    return path, hash


def get_delete_list(local_book_path_list):

    local_book_path_set = set(local_book_path_list)
    db_book_path_list, db_book_hash_list = get_db_book_list()
    db_book_path_set = set(db_book_path_list)
    diff_set = db_book_path_set.difference(local_book_path_set)
    return list(diff_set)


def get_file_size(file_path):
    size_in_bytes = os.path.getsize(file_path)
    size_in_mb = size_in_bytes / (1024 * 1024)
    if size_in_mb > 1:
        return '{:.2f}MB'.format(size_in_mb)
    else:
        return '{:.2f}KB'.format(size_in_mb * 1024)


def get_file_sha256(file_path):
    with open(file_path, 'rb') as f:
        sha256obj = hashlib.sha256()
        sha256obj.update(f.read())
        file_sha256 = sha256obj.hexdigest()
    return file_sha256


@timer_decorator
def get_file_recursive(filepath):
    #递归遍历filepath下所有文件，包括子目录

    files = os.listdir(filepath)
    for item in files:
        target_item = os.path.join(filepath, item)
        if os.path.isdir(target_item):
            get_file_recursive(target_item)
        else:
            # print(target_item)
            path = target_item.replace('/', '\\').replace('\\\\ttnas\\电子书', '')
            local_book_path_list.append(path)
            if path not in db_book_path_list:
                name = target_item.split('\\')[-1]
                size = get_file_size(target_item)
                hash = get_file_sha256(target_item)

                if hash in db_book_hash_list:
                    update_list.append({'update_book_name': name, 'update_book_path': path, 'update_book_hash': hash})
                else:
                    insert_list.append({'book_name': name, 'book_path': path, 'book_size': size, 'book_hash': hash})
                # if hash in db_book_hash_list:
                #     pass
                print(name, path, size, hash)


#递归遍历指定目录下所有文件
Base.metadata.create_all(engine)
db_book_path_list, db_book_hash_list = get_db_book_list()
get_file_recursive('//ttnas/电子书')
print('insert_list========>:' + str(len(insert_list)))
print(insert_list)
insert_values(insert_list)
print('update_list========>:' + str(len(update_list)))
print(update_list)
update_values(update_list)
delete_list = get_delete_list(local_book_path_list)
print('delete_list========>:' + str(len(delete_list)))
print(delete_list)
delete_values(delete_list)

# truncate_table()
# drop_table()
# select_values('f2f44f6c33be3b423d8bfad22eb705df33fa23e209b28c71712f30344fb598c9')
