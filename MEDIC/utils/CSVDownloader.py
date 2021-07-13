import _io
import io

import pandas as pd
import requests


class CsvDownloader:
    def __init__(self, origin_server_url: str):
        self.origin_server_url = origin_server_url

    def get_response(self):
        return requests.get(self.origin_server_url)

    def get_csv_string(self, response: requests.models.Response = None):
        if response is None:
            return io.StringIO(self.get_response().text)

        return io.StringIO(response.text)

    def get_dataFrame(self, csv_string: _io.StringIO = None ):
        if csv_string is None:
            return pd.read_csv(self.get_csv_string())

        return pd.read_csv(csv_string)
