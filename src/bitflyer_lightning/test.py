import requests


def main():
    get_markets()
    # get_board()
    get_ticker()
    get_execution()
    get_health()
    # get_chat()


def get_markets():
    path = '/v1/getmarkets'
    url = end_point + path
    response = requests.get(url)
    print(response.json())


# 板情報
def get_board():
    path = '/v1/board'
    url = end_point + path
    response = requests.get(url)
    print(response.json())


def get_ticker():
    path = '/v1/ticker'
    url = end_point + path
    response = requests.get(url)
    print(response.json())


# 約定履歴
def get_execution():
    path = '/v1/getexecutions'
    url = end_point + path
    payload = {'count': '1'}
    response = requests.get(url, payload)
    print(response.json())


def get_health():
    path = '/v1/gethealth'
    url = end_point + path
    response = requests.get(url)
    print(response.json())


def get_chat():
    path = '/v1/getchats'
    url = end_point + path
    payload = {'from_date': '1'}
    response = requests.get(url, payload)
    print(response.json())


if __name__ == '__main__':
    end_point = 'https://api.bitflyer.jp'
    main()
