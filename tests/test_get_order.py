from src import api_rquests, data


def get_order_creation_body():
    current_body = data.order_creation_body.copy()
    return current_body


def create_order():
    body = get_order_creation_body()
    res = api_rquests.create_order(body)
    return res.json()['track']


def positive_assert():
    track_number = create_order()
    res = api_rquests.get_order(track_number)

    assert res.status_code == 200


def test_get_order_description():
    positive_assert()
