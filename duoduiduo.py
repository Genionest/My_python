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

from sqlalchemy import Column,Integer,String,ForeignKey,Table#Column对应列，Integer，String对应INT，ForeignKey为外键,Table为创建表的方法
from sqlalchemy.orm import relationship#relationship关联两个表
#关联多对多的两个表，先建立一个关系表
test = Table('tset',Base.metadata,
             
             Column('id',Integer,primary_key=True),
             Column('name',String(100)))

stu_course = Table('stu_course',Base.metadata,
                   Column('s_id',Integer,ForeignKey('students.s_id'),primary_key=True),#两个列表都设置主键，
                   Column('c_id',Integer,ForeignKey('course.c_id'),primary_key=True))  #这样就形成了主键对

class Students(Base):
    __tablename__ = 'students'
    s_id = Column(Integer,primary_key=True)
    s_name = Column(String(100))

    course = relationship('Course',secondary=stu_course)#secondary关联第二关联表，这里关联的是关系表

class Course(Base):
    __tablename__ = 'course'
    c_id = Column(Integer,primary_key=True)
    c_name = Column(String(100))

    course = relationship('Students',secondary=stu_course)#secondary关联第二关联表，这里关联的是关系表

Base.metadata.create_all()

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(engine)
session = Session()

stu1 = Students(s_name='xxx')
stu2 = Students(s_name='hhh')

cour1 = Course(c_name='PYTHON')
cour2 = Course(c_name='JAVA')

stu1.course.extend([cour1,cour2])#stu1.course为列表，所以可以使用列表的方法
stu2.course.append(cour2)

session.add(stu1)
session.add(stu2)

session.commit()
