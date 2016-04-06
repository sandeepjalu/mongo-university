
import pymongo
import sys
from array import *

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db=connection.students
grades = db.grades


def find():

    print "find, reporting for duty"

    query = {}

    try:

        cursor = grades.find({'type':'homework'})
        
        #cursor = cursor.sort('student_id', pymongo.ASCENDING).skip(4).limit(1)
        
        cursor = cursor.sort([('student_id',pymongo.ASCENDING),
                              ('score',pymongo.ASCENDING)])
        

    except Exception as e:
        print "Unexpected error:", type(e), e
    arr=[]
    for doc in cursor:
        temp = doc['student_id']
        _id = doc['_id']
        if temp not in arr:
            arr.append(temp)
            grades.remove({'_id':_id})
            #print doc
            #print arr

find()

