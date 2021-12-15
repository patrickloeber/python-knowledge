# TinyDB
# A tiny and simple database for small projects
# simple API
# Document oriented: Use any document (e.g. json), represented a dict
# Written in pure Python with full test coverage, no other dependency

# Do not use for bigger projects where performance matters, 
# or advanced db features are needed

# Installation:
# pip install tinydb

from tinydb import TinyDB, Query
db = TinyDB('db.json')

User = Query() # type: tinydb.queries.Query

def insert_user():
    db.insert({'name': 'John', 'age': 22})
    db.insert({'name': 'Max', 'age': 25})
    db.insert({'name': 'Sarah', 'age': 21, 'city': 'New York'})
    #use insert_multiple() to insert more then one document
    db.insert_multiple([{'name': 'Jessy', 'age': 20}, {'name': 'Mark', 'age': 27}])

def search_user():
    results = db.search(User.city == 'New York') # returns a list
    for res in results:
        print(res) # type: tinydb.database.Document
        # print(res.city) # Not allowed!
        print(res['city'])

    results = db.search(User.age > 21)
    for res in results:
        print(res)

def update_user():
    db.update({'age': 26}, User.name == 'Max')
    #use update_multiple() to update more then one document
    db.update_multiple([({'age': '21'}, User.name == 'Jessy'),({'age': '28'}, User.name == 'Mark')])
    for item in db:
        print(item)

    # or
#    results = db.search(User.name == 'Max')
#    for res in results:
#        res['age'] = 27
#    db.write_back(results) # write back results we retrieved

    # or get and update/remove by document_id

def delete_user():
    db.remove(User.name == 'John')
    # db.purge() # remove all

def update_by_document_id():
    #db.remove(doc_ids=[2])
    # this will not create doc_id=2, but the next highest number
    #db.insert({'name': 'Jason', 'age': 40})

    item = db.get(doc_id=3)
    print(item)
    print(item.doc_id)

    db.update({'city': 'Boston'}, doc_ids=[1, 2])

    #db.remove(doc_ids=[1, 2])


#### TESTS ####

#db.purge() # empty db
#purge() is giving error
#you can use truncate() instead
#db.truncate()


#insert_user()
#search_user()
#update_user()
#delete_user()
#update_by_document_id()

#print(db.all())
#for item in db:
#    print(item)
#print(len(db)) # number of items
