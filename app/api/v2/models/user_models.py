from urllib.parse import urlparse

class UserInfo:
    """ Defines the user information """
    def __init__(self, firstname, lastname, othername, username, email, phoneNumber, password, isAdmin):
        self.db_config = os.getenv('api_database_url')
        self.response = urlparse(self.db_config)
        self.config = {
            'database': self.response.path[1:],
            'user': self.response.username,
            'password': self.response.password,
            'host': self.response.hostname
        }
        self.firstname = firstname
        self.lastname = lastname
        self.othername = othername
        self.username = username
        self.email = email
        self.phoneNumber = phoneNumber
        self.password = password 
        self.isAdmin = isAdmin  

    def add_user(self):
        con, response = psycopg2.connect(**self.config), None
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            query = "INSERT INTO users ( firstname, lastname, othername, username, email, phoneNumber, password, isAdmin) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *; "
            cur.execute(query, (
                self.firstname, 
                self.lastname,
                self.othername,
                self.username,
                self.email,
                self.phoneNumber,
                self.password,
                self.isAdmin
            ))
            con.commit()
            response = cur.fetchone()
        except Exception as e:
            con.close()
        con.close()
        return response