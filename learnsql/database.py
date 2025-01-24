import pandas as pd
from urllib.parse import quote_plus as urlquote
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import text
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from typing import List
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import select

password = 'qwe123!@#'
sql = "select index_code,index_code_clean,index_short_name,index_full_name from etf_index_code"
pwd = urlquote(password)
engine = create_engine("mysql+pymysql://flaskapi:{}@192.168.1.5:3306/flaskapi?charset=utf8mb4".format(pwd), echo=True)

# china_index_list = pd.read_sql(sql, engine)
# print(china_index_list.to_string())

# with engine.connect() as conn:
#     result = conn.execute(text("select index_code,index_code_clean,index_short_name,index_full_name from etf_index_code"))
#     #     print(result.all())
#     # print(result.mappings())
#     for i in result.mappings():
#         print(i)

# with engine.connect() as conn:
#     conn.execute(text("CREATE TABLE some_table (x int, y int)"))
#     conn.execute(
#         text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
#         [{
#             "x": 1,
#             "y": 1
#         }, {
#             "x": 2,
#             "y": 4
#         }],
#     )
#     conn.commit()

# with engine.begin() as conn:
#     conn.execute(
#         text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
#         [{
#             "x": 6,
#             "y": 8
#         }, {
#             "x": 9,
#             "y": 10
#         }],
#     )

# with engine.connect() as conn:
#     result = conn.execute(text("show tables"))
#     print(result.all())

# stmt = text("SELECT x, y FROM some_table WHERE y > :y ORDER BY x, y")
# with Session(engine) as session:
#     result = session.execute(stmt, {"y": 6})
#     for row in result:
#         print(f"x: {row.x}  y: {row.y}")

# with Session(engine) as session:
#     result = session.execute(
#         text("UPDATE some_table SET y=:y WHERE x=:x"),
#         [{
#             "x": 9,
#             "y": 11
#         }, {
#             "x": 13,
#             "y": 15
#         }],
#     )
#     session.commit()

# metadata_obj = MetaData()
# user_table = Table(
#     "user_account",
#     metadata_obj,
#     Column("id", Integer, primary_key=True),
#     Column("name", String(30)),
#     Column("fullname", String(30)),
# )

# metadata_obj.create_all(engine)
# metadata_obj.drop_all(engine)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user_account"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]] = mapped_column(String(30))

    # addresses: Mapped[List["Address"]] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


# class Address(Base):
#     __tablename__ = "address"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     email_address: Mapped[str] = mapped_column(String(30))
#     user_id = mapped_column(ForeignKey("user_account.id"))
#     user: Mapped[User] = relationship(back_populates="addresses")

#     def __repr__(self) -> str:
#         return f"Address(id={self.id!r}, email_address={self.email_address!r})"

Base.metadata.create_all(engine)
print(select(User.name, User.fullname))