from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship, sessionmaker


DATABASE_URL = "postgresql+psycopg2://postgres:mdkn@localhost:5432/vision_analysis"

engine = create_engine(DATABASE_URL, echo = True)

