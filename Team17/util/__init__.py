import sqlite3

from Team17.config import file_config
from Team17.util import logger

log = logger.getLogger(__name__)
config = file_config()

DB = config.get('DB','dbname')

def fetch_query(query):
    try:
        log.info("connecting db")
        conn = sqlite3.connect(DB)
        c = conn.cursor()
        log.info("executing querry")
        res = c.execute(query)
        return res.fetchall()
    except Exception as e:
        log.error('something went wrong: {}'.format(e))
        return None


def update_query(query):
    try:
        log.info("connecting db")
        conn = sqlite3.connect(DB)
        c = conn.cursor()
        log.info("executing querry")
        c.execute(query)
        conn.commit()
        return True
    except Exception as e:
        log.error('something went wrong: {}'.format(e))
        return False
