import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

DATABASE = 'database.db'

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            DATABASE,
            #o sqlite3 tentará converter os tipos de coluna do SQLite para um tipo Python correspondente.
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        # para que os dados retornem em estilo de dicionario
        g.db.row_factory = sqlite3.Row

    return g.db

def insert(args=()):
    sql = ''' INSERT INTO countries(country_name,capital)
              VALUES(?,?) '''
    cur = get_db().cursor()
    cur.execute(sql, args)
    get_db().commit()
    return cur.lastrowid
    
def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = [dict((cur.description[i][0], value) \
       for i, value in enumerate(row)) for row in cur.fetchall()]
   
    get_db().commit()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
        
def init_db():
    db = get_db()
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')