from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

db_url = os.getenv("DATABASE_URL")
engine = create_engine(db_url) # type: ignore
sessionLocal = sessionmaker(autoflush=False,autocommit = False, bind=engine)