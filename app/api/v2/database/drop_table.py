drop_tables = (
    """ DROP TABLE IF EXISTS users CASCADE """,
    """ DROP TABLE IF EXISTS meetups CASCADE """,
    """ DROP TABLE IF EXISTS questions CASCADE """,
    """ DROP TABLE IF EXISTS reservations CASCADE """,
    """ DROP TABLE IF EXISTS comments CASCADE """
)

drop_tables_command = drop_tables