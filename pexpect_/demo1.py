import pexpect
import sys

child = pexpect.spawn('ssh root@192.168.253.136')
child.logfile = sys.stdout.buffer
child.expect('password:')
child.sendline('1qaz@WSX')
child.expect("#")
child.sendline("ls /root")
child.expect("#")
child.sendline("exit")
