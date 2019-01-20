create_tables = (
    """ 
    CREATE TABLE IF NOT EXISTS users(
    id SERIAL PRIMARY KEY,
    firstname VARCHAR(255) NOT NULL,
    lastname VARCHAR(255) NOT NULL,
    othername VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phoneNumber VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    registered timestamp with time zone DEFAULT now(),
    isAdmin BOOLEAN NOT NULL
    ) 
    """,
    """ 
    CREATE TABLE IF NOT EXISTS meetups(
    id SERIAL PRIMARY KEY,
    createdOn timestamp with time zone DEFAULT now(),
    user_id INTEGER NOT NULL,
    location VARCHAR(255) NOT NULL,
    images VARCHAR(255) NOT NULL,
    topic VARCHAR(255) NOT NULL,
    happeningOn VARCHAR(255) NOT NULL,
    tags VARCHAR(255) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
    ) 
    """,
    """ 
    CREATE TABLE IF NOT EXISTS question(
    id SERIAL PRIMARY KEY,
    createdOn timestamp with time zone DEFAULT now(),
    createdBy INTEGER NOT NULL,
    meetup_id INTEGER NOT NULL,
    title VARCHAR(255) NOT NULL,
    body VARCHAR(255) NOT NULL,
    votes INTEGER NOT NULL,
    FOREIGN KEY (meetup_id) REFERENCES meetups (id) ON DELETE CASCADE
    ) 
    """,
    """ 
    CREATE TABLE IF NOT EXISTS reservations(
    id SERIAL PRIMARY KEY,
    createdOn timestamp with time zone DEFAULT now(),
    user_id INTEGER NOT NULL,
    meetup_id INTEGER NOT NULL,
    topic VARCHAR(255) NOT NULL,
    status VARCHAR(255) NOT NULL,
    FOREIGN KEY (meetup_id) REFERENCES meetups (id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
    ) 
    """,
    """ 
    CREATE TABLE IF NOT EXISTS comments(
    id SERIAL PRIMARY KEY,
    createdOn timestamp with time zone DEFAULT now(),
    user_id INTEGER NOT NULL,
    question_id INTEGER NOT NULL,
    comments VARCHAR(255) NOT NULL,
    FOREIGN KEY (question_id) REFERENCES question (id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
    ) 
    """,
    """ 
    CREATE TABLE IF NOT EXISTS tags(
    id SERIAL PRIMARY KEY,
    createdOn timestamp with time zone DEFAULT now(),
    meetup_id INTEGER NOT NULL,
    topic VARCHAR(255) NOT NULL,
    tag_item VARCHAR(255) NOT NULL,
    FOREIGN KEY (meetup_id) REFERENCES meetups (id) ON DELETE CASCADE
    ) 
    """,
    """ 
    CREATE TABLE IF NOT EXISTS images(
    id SERIAL PRIMARY KEY,
    createdOn timestamp with time zone DEFAULT now(),
    meetup_id INTEGER NOT NULL,
    topic VARCHAR(255) NOT NULL,
    image VARCHAR(255) NOT NULL,
    FOREIGN KEY (meetup_id) REFERENCES meetups (id) ON DELETE CASCADE
    ) 
    """

)
create_tables_command = create_tables
