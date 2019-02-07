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

from sqlalchemy import Column,Integer,String,Text,Boolean,Date,DateTime#导入各种类型
from datetime import datetime,date#导入python中相对应的date，datetime类

class Students(Base):
    __tablename__ = 'students'

    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(100),nullable=False)
    gender = Column(Boolean)
    admision_time  = Column(DateTime,default=datetime.now)
    birth_date = Column(Date)
    article = Column(Text)

Base.metadata.create_all()#映射进MySQL

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(engine)
session = Session()

stu1 = Students(name='lily',gender=False,birth_date=date(1999,12,12),article='justforit')
session.add(stu1)
session.commit()
