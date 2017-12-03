import paramiko
import pwn

if __name__ == '__main__':
    host = 'ctfq.sweetduet.info'
    username = 'q4'
    password = 'q60SIMpLlej9eq49'

    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password, look_for_keys=False, allow_agent=False, port=10022)

    stdin, stdout, stderr = client.exec_command('ls -l')

    for o in stdout:
        print(o)

