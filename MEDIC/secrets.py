from MEDIC.secrets_app import MARIA_DB_USER, MARIA_DB_PASSWORD, MARIA_DB_ADDRESS, MARIA_DB_PORT
from MEDIC.utils.DBConnector import DBController

controller = DBController(user=MARIA_DB_USER,
                          password=MARIA_DB_PASSWORD,
                          address='{addr}:{port}'.format(addr=MARIA_DB_ADDRESS, port=MARIA_DB_PORT),
                          database='covid_info')
