#!/usr/bin/env python
import psycopg2
from psycopg2 import extensions
from app import app,db

# try:
#     conn = psycopg2.connect(
#         host="localhost",
#         port="5432",
#         user="postgres",
#         password="santiago2000"
#     )

#     conn.set_isolation_level(extensions.ISOLATION_LEVEL_AUTOCOMMIT)

#     cursor = conn.cursor()

#     cursor.execute("CREATE DATABASE todo")

#     cursor.close()
#     conn.close()
# except:
#     pass

app.app_context().push()
db.create_all()
