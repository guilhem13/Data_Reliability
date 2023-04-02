import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask

load_dotenv()  # loads variables from .env file into environment

app = Flask(__name__)
url = os.environ.get("DATABASE_URL")  # gets variables from environment
connection = psycopg2.connect(url)