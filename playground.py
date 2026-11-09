# Here python will directly communicate with postgre with any fastapi endpoints

import os 
from dotenv import load_dotenv
from sqlalchemy import create_engine,text

# Step1 : Get the url from env file
load_dotenv()
db_url = os.getenv("DATABASE_URL")
print(db_url)

#Step 2: engine = road to the database
engine = create_engine(db_url)
with engine.connect as connection:
    version = connection.execute(text("Select version()"))







