import os

from googleapiclient import discovery
from oauth2client import tools
from oauth2client import client
from oauth2client.file import Storage

try:
    import argparse

    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None
import httplib2
import sys

SCOPES = "https://www.googleapis.com/auth/gmail.readonly"
CLIENT_SECRET_FILE = "client_secret.json"
APPLICATION_NAME = "MyGmailReceiver"


def get_credential():
    # 自分のパス入れる
    script_dir = os.path.abspath(os.path.dirname(__file__))
    # credentials のパス入れる
    credential_dir = os.path.join(script_dir, ".credentials")
    # credentialsなかったらパス作る
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    # 情報入ったjsonのパス入れる
    credential_path = os.path.join(credential_dir, "my-gmail-receiver.json")
    # Storageの概念はよくわからんが、とりあえずcredentials にjsonで認証情報入れてる
    store = Storage(credential_path)
    credentials = store.get()

    # この下よくわからん。FLOWの概念とか
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else:
            credentials = tools.run(flow, store)
        print("Storing credentials to " + credential_path)

    return credentials


def main():
    # 認証情報入れる
    credentials = get_credential()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            print(label['name'])


if __name__ == '__main__':
    main()
