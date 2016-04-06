
import pymongo
import sys
from array import *

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db=connection.school
students = db.students


def find():

    print "find, function Called :)"

    query = {}

    try:

        cursor = students.find()
        
        #cursor = cursor.sort('student_id', pymongo.ASCENDING).skip(4).limit(1)
        
        #cursor = cursor.sort([('_id',pymongo.ASCENDING)])
        

    except Exception as e:
        print "Unexpected error:", type(e), e
    for doc in cursor:
        _id = doc['_id']
        arr = doc['scores']
        #print arr
        #print 'Hello'
        temp = 999
        for i in arr:
            print i
            if i['type'] == 'homework' and float(i['score']) < temp:
                ind = arr.index(i)
                temp = i['score']
        #print arr.pop(ind)
        print students.update_one({'_id':_id},{'$set':{'scores':arr}})
        #print arr
        #arr = []
        #print arr
find()

