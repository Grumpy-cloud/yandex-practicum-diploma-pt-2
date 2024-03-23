import requests

from src import configuration as cfg
from src import data


# ========POST========= #
def create_order(body):
    return requests.post(cfg.URL + cfg.CREATE_ORDER,
                         json=body,
                         headers=data.headers)


# ========GET========== #
def get_order(track_number):
    return requests.get(cfg.URL + cfg.GET_ORDER.format(track_number),
                        headers=data.headers)
# ===================== #
