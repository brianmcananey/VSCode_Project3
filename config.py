import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{os.getenv('brianmcananey')}:{os.getenv('')}@{os.getenv('localhost')}/{os.getenv('login_msp3')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
