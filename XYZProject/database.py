

import csv
import os
import pymysql

from flask_app import Salaries, database1
os.environ['KAGGLE_USERNAME'] = "yadhukm46"
os.environ['KAGGLE_KEY'] = "2a3f7cadc80fd4394670a17c8e07ce82"
from kaggle.api.kaggle_api_extended import KaggleApi
api = KaggleApi()
api.authenticate()
#api.dataset_list_files('Cornell-University/arxiv').files
api.dataset_download_files('saurabhshahane/data-science-jobs-salaries', path=".")

from zipfile import ZipFile 
with ZipFile('data-science-jobs-salaries.zip', 'r') as zipObj:    # Extract all the contents of zip file in current directory   
    zipObj.extractall()
mydb = db = pymysql.connect("ykm2478.mysql.pythonanywhere-services.com",
    "ykm2478",
    "YadhuKM1",
    "ykm2478$DataXYZ")
cursor = mydb.cursor()
csv_data = csv.reader(open('Data Science Jobs Salaries.csv'))
for row in csv_data:

    cursor.execute('INSERT INTO salaries(work_year,experience_level,employment_type,job_title, \
          salary,salary_currency,salary_in_usd,employee_residence,remote_ratio,company_location ,company_size,)' \
          'VALUES("%s", "%s", "%s","%s", "%s", "%s","%s", "%s", "%s","%s", "%s", "%s")', 
          row)
database1.commit()
#close the connection to the database.
cursor.close()
#kaggle datasets download -d saurabhshahane/data-science-jobs-salaries
#{"username":"yadhukm46","key":"2a3f7cadc80fd4394670a17c8e07ce82"}