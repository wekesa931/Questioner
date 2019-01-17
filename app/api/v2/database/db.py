drop_tables = (
    """ DROP TABLE IF EXISTS users CASCADE """
    """ DROP TABLE IF EXISTS meetups CASCADE """
    """ DROP TABLE IF EXISTS questions CASCADE """
)

create_tables = (
    """ 
    CREATE TABLE IF NOT EXISTS users(
    user_id SERIAL PRIMARY KEY,
    firstname VARCHAR(255) NOT NULL,
    lastname VARCHAR(255) NOT NULL,
    othername VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phoneNumber INTEGER NOT NULL,
    password VARCHAR(255) NOT NULL,
    registered timestamp with time zone DEFAULT now(),
    isAdmin BOOLEAN NOT NULL
    ) 
    """,
    """ 
    CREATE TABLE IF NOT EXISTS meetups(
    meetup_id SERIAL PRIMARY KEY,
    createdOn timestamp with time zone DEFAULT now(),
    location VARCHAR(255) NOT NULL,
    images VARCHAR(255) NOT NULL,
    topic VARCHAR(255) NOT NULL,
    happeningOn TIMESTAMP NOT NULL,
    tags VARCHAR(255) NOT NULL
    
    ) 
    """,
    """ 
    CREATE TABLE IF NOT EXISTS question(
    question_id SERIAL PRIMARY KEY,
    createdOn timestamp with time zone DEFAULT now(),
    createdBy VARCHAR(255) NOT NULL,
    meetup_id INTEGER NOT NULL,
    title VARCHAR(255) NOT NULL,
    body VARCHAR(255) NOT NULL,
    votes INTEGER NOT NULL
    ) 
    """

)
create_tables_command = create_tables