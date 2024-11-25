import os
from dotenv import load_dotenv


load_dotenv()


DATABASE_URL = os.getenv('DATA_URL')
SINGLE_IDENTIFIER = os.getenv('SINGLE_IDENTIFIER')
DB_STRING = os.getenv('CONNECTION_STRING')