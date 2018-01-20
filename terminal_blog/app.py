from database import Database
from models.post import post

__author__ = 'jslvtr'


Database.initialize()
 
post =Blog(author="jose",
            title="sample title",
            description="sample descrption")
             

blog.new_post()

blog.save_to_mongo()

Blog.from_mongo()

blog.get_posts()
    