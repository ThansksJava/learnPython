from fabric.api import run, env, cd
env.hosts = ['192.168.253.136']
env.user = "root"
env.port = '22'
env.password = '1qaz@WSX'


def host_type():
    run("uname -s")


def date():
    run("date")
