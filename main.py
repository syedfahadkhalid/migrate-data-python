import datetime
from migrate_data import MigrateData
from configs import Config
import logging



def main():

    Config().load_configs()
    logging.info(f'Script Start Time: {datetime.datetime.now()}')
    MigrateData().migrate_data()
    logging.info(f'Script End Time: {datetime.datetime.now()}')



if __name__ == "__main__":
    main()
