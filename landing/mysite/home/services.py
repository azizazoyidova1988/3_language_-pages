from django.db import connection
from contextlib import closing


def get_posts(CODE):
    with closing(connection.cursor()) as cursor:
        cursor.execute(f"""select title_{CODE} as title,description_{CODE} as description,image from home_post""")
        posts = dict_fetchall(cursor)
        return posts

def get_followers(CODE):
    with closing(connection.cursor()) as cursor:
        cursor.execute(f"""select full_name_{CODE} as full_name,comment_{CODE} as comment,image from home_follower""")
        followers = dict_fetchall(cursor)
        return followers

def dict_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def dict_fetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))