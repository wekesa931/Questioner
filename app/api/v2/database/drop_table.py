drop_tables = (
    """ DROP TABLE IF EXISTS users CASCADE """,
    """ DROP TABLE IF EXISTS meetups CASCADE """,
    """ DROP TABLE IF EXISTS question CASCADE """,
    """ DROP TABLE IF EXISTS reservations CASCADE """,
    """ DROP TABLE IF EXISTS comments CASCADE """,
    """ DROP TABLE IF EXISTS tags CASCADE """,
    """ DROP TABLE IF EXISTS images CASCADE """
)

drop_tables_command = drop_tables