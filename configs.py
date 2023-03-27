from env_variables import config_file_name
import yaml
import logging


class Config:

    def load_configs(self):
        self.set_logging_config()
        logging.info("Fetching Configurations")

        configurations = yaml.load(open(config_file_name), Loader=yaml.FullLoader)
        Config.db_url = configurations.get("db_url")
        Config.db_username = configurations.get("db_username")
        Config.db_password = configurations.get("db_password")
        Config.db_port = configurations.get("db_port")
        Config.schema = configurations.get("schema")
        Config.start = configurations.get("start")
        Config.end = configurations.get("end")
        Config.batch_size = configurations.get("batch_size")

    @staticmethod
    def set_logging_config():
        logging.basicConfig(
            format='%(asctime)s %(levelname)-8s %(message)s',
            level=logging.DEBUG,
            datefmt='%Y-%m-%d %H:%M:%S'
        )
