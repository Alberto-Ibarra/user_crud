from mysqlconnection import connectToMySQL

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']

    def fullname(self):
        return f"{self.first_name.capitalize()} {self.last_name.capitalize()}"

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('mydb').query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL('mydb').query_db(query,data)
        print(results)
        if results:
            return cls(results[0])

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( first_name , last_name , email  ) VALUES ( %(first_name)s , %(last_name)s , %(email)s  );"
        return connectToMySQL('mydb').query_db( query, data )

    @classmethod
    def update(cls,data):
        query = "UPDATE users SET first_name =%(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;"

        return connectToMySQL('mydb').query_db( query,data )

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM users WHERE id = %(id)s"
        return connectToMySQL('mydb').query_db(query,data)