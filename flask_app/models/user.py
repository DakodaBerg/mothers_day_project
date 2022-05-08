from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, bcrypt       
from flask import flash, session

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id  = data['id']
        self.name  = data['name']

        
    #Create
    @classmethod
    def create(cls, data:dict) -> int:
        query = "INSERT INTO users(name)values(%(name)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
        
    #Read
    @classmethod
    def get_all(cls) -> list:
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            all_users = []
            for user in results:
                all_users.append(cls(user))
            return all_users
        return False
    #Read
    @classmethod
    def get_one(cls, data:dict) -> list:
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            return cls(results[0])
        return False

    #Update
    @classmethod
    def update_one(cls, data:dict) -> None:
        query = "UPDATE users SET name = %(name)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    #Delete
    @classmethod
    def delete_one(cls, data:dict) -> None:
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)