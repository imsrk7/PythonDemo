import paramiko as paramiko

from Utilities.configurations import *

host = getConfig()['Server']['host']
port = getConfig()['Server']['port']
username = getConfig()['Server']['username']
password = getConfig()['Server']['password']

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

# Run Commands
# stdin, stdout, stderr = ssh.exec_command("ls -a")
stdin, stdout, stderr = ssh.exec_command("cat demofile")
# print(stdout.readlines())
line = stdout.readlines()
print(line[1])

# Upload Files by using SFTP protocol
sftp = ssh.open_sftp()
destinationPath = "script.py"
localPath = "C:\\Users\\Srk\\PycharmProjects\\PythonDemo\\batchFile\\script.py"
sftp.put(localPath, destinationPath)

destinationPath = "loanasa.csv"
localPath = "C:\\Users\\Srk\\PycharmProjects\\PythonDemo\\batchFile\\loanasa.csv"
sftp.put(localPath, destinationPath)

# Triggered the batch Commands
stdin, stdout, stderr = ssh.exec_command("python3 script.py")

# Downloading file from server
sftp.get("loanasa.csv", "C:\\Users\\Srk\\PycharmProjects\\PythonDemo\\batchFile\\OutputFile\\loanasa.csv")

ssh.close()
