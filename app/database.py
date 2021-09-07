# 데이터베이스와 연결시켜주는 로직

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.my_settings import SQLALCHEMY_DATABASE_URL


SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL) # sqlalchemy engine 생성 -> main.py에서 사용
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # SessionLocal 클래스의 인스턴스를 생성하면 실제 DB에 접근해서 CRUD 가능

Base = declarative_base() # 이 클래스에서 상속하여 각 DB 모델 또는 클래스를 만든다.
