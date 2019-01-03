from sqlalchemy import create_engine
#创建连接
HOSTNAME = '127.0.0.1' #ip address，本地连接为127.0.0.1
PORT = '3306' #端口，默认为3306
DATABASE = 'z_db'
USERNAME = 'root'
PASSWORD = 'root'

#DB_URI的格式：数据库类型+数据库驱动名称：//用户名：密码@机器地址：端口号/数据库名
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
#？charset=utf8将编码设置为utf-8
engine = create_engine(DB_URI)

#创建类
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base(engine)#创建基类

from sqlalchemy import Column,Integer,String#Column对应列，Integer，String对应INT，

class User(Base):#创建的这些表类必须继承基类
    __tablename__ = 'user'#为表命名
    id = Column(Integer,primary_key=True,autoincrement=True)
    username = Column(String(50))
    password = Column(String(100))

    def __repr__(self):
        return '<User(id="%s",username="%s",password="%s")>' %(self.id,self.username,self.password)

Base.metadata.create_all()#将表输入数据库

#创建session会话
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(engine)
session = Session()

#增加
def add_user():
    user1 = User(password='root')#创建数据
    session.add(user1)
    #session.add_all([
        #User(username='aaaa',password='1111'),
        #User(username='bbbb',password='2222'),
        #User(username='cccc',password='3333'),
        #User(username='dddd',password='4444')
    #])
    session.commit()
#add_user()
#查找
def search_user():
    rs = session.query(User).all()#有.all()的返回的是一个列表对象
    rs = session.query(User).first()#没有.all()的返回的是一个类
    rs = session.query(User).filter_by(username='wargon').all()#这里必须要加.all()，这样返回的是一个列表
    rs = session.query(User).get(2)#用主键查找对象
    rs = session.query(User).filter(User.username=='wargon').all()#filter引用列名时，使用的是‘类.属性名’，比较符号用‘==’
    print(rs)                                                      #filter_by直接用属性名，比较符号用“=”
#改动
def update_user():
    user = session.query(User).filter_by(id=3)[0]#因为filter返回的是一个列表，所以用一个[0]
    print(user)
    user.username = 'wowowo'
    session.commit()
#删除
def delete_user():
    user = session.query(User).filter_by(username='wargon').first()
    print(user)
    session.delete(user)
    session.commit()
#查询方法
rs = session.query(User).filter(User.username=='wargon').all()#等于
rs = session.query(User).filter(User.username!='wargon').all()#不等于
rs = session.query(User).filter(User.username.like('%a%')).all()#模糊查询
rs = session.query(User).filter(User.username.in_(['wargon','沃艮'])).all()#成员属于
#非成员属于
rs = session.query(User).filter(~User.username.in_(['wargon','沃艮'])).all()
rs = session.query(User).filter(User.username.notin_(['wargon','沃艮'])).all()
#是否为空
rs = session.query(User).filter(User.username==None).all()#为空
rs = session.query(User).filter(User.username.is_(None)).all()#为空
rs = session.query(User).filter(User.username!=None).all()#不为空
rs = session.query(User).filter(~User.username.is_(None)).all()#不为空
#多个条件
rs = session.query(User).filter(User.username=='wargon',User.password=='root').all()#and多条件
rs = session.query(User).filter_by(username='wargon',password='root').all()#and多条件
from sqlalchemy import or_#导入or_模块
rs = session.query(User).filter(or_(User.username=='wargon',User.username=='沃艮')).all()#或多条件

print(rs)