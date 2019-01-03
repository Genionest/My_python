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

from sqlalchemy import Column,Integer,String,ForeignKey#Column对应列，Integer，String对应INT，ForeignKey为外键
from sqlalchemy.orm import relationship#relationship关联两个表
class Department(Base):
    __tablename__ = 'department'

    id = Column(Integer,primary_key=True,autoincrement=True)
    d_name = Column(String(100))

    def __repr__(self):
        return '<User(id="%s",d_name="%s",)>' %(self.id,self.d_name)


class Student(Base):
    __tablename__ = 'student'

    s_id = Column(Integer,primary_key=True,autoincrement=True)
    s_name = Column(String(100))
    d_id = Column(Integer,ForeignKey('department.id'))

    department = relationship('Department',backref='student')#一对多关系，仅在一个类里面使用relationship和backref即可
    stu_details = relationship('Stu_details',uselist=False)#uselist=False不为列表，一对一关系，两个类里面都要用relationship
    def __repr__(self):
        return '<User(s_id="%s",s_name="%s",d_id="%s")>' %(self.s_id,self.s_name,self.d_id)

class Stu_details(Base):
    __tablename__ = 'stu_details'

    id = Column(Integer,primary_key=True)
    age = Column(Integer)
    city = Column(String(100))
    s_id = Column(Integer,ForeignKey('student'))

    student =  relationship('Student')#一对一关系，两个类里面都要用relationship

Base.metadata.create_all()

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(engine)
session = Session()

rs = session.query(Student).first()
print(rs.stu_details)
#session.add(Department(d_name='AAAA'))
#session.commit()
#session.add(Student(s_name='haha',d_id=1))
#session.commit()

#rs = session.query(Department).first()
#s1 = Student(s_name='meimei')

#rs.student.append(s1)#rs为列表，可直接在里面添加列元素
#session.commit()#用append方法添加列，也要使用session.commit
#print(rs.student)
