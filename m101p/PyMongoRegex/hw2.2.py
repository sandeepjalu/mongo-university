
import pymongo
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db=connection.students
grades = db.grades


def find():

    print "find, reporting for duty"

    query = {}

    try:

        cur = grades.find()#.sort({'student_id':1})#.sort({'score':1})
        cursor = cur.sort({'student_id':1})
    except Exception as e:
        print "Unexpected error:", type(e), e

    for doc in cursor:
        print doc

find()

