from pexpect import pxssh
import sys

s = pxssh.pxssh()
s.logfile = sys.stdout.buffer
hostname = '192.168.253.136'
username = 'root'
password = '1qaz@WSX'
s.login(hostname, username, password)
# s.prompt()
s.sendline("ls /")
# s.prompt()
s.sendline("whoami")
s.logout()
