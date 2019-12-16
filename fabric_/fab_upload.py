from fabric.api import *
env.hosts = ['192.168.253.136', '192.168.253.137']
env.user = "root"
env.port = '22'
env.password = '1qaz@WSX'


# compress local file and this function only run once
@task
@runs_once
def compress_local():
    local("tar zcvf ./fabfile.tar.gz ./fabfile.py")


# upload to remote server
@task
def put_task():
    run("rm -rf /home/testdemo && mkdir /home/testdemo")
    with cd("/home/testdemo"):
        put("/home/fengjie/workspace/learnPython/fabric_/fabfile.tar.gz","/home/testdemo/fabfile.tar.gz")


# check the uploaded file
@task
def check_task():
    localmd5 = local("md5sum /home/fengjie/workspace/learnPython/fabric_/fabfile.tar.gz", capture=True).split(" ")[0]
    remotemd5 = run("md5sum /home/testdemo/fabfile.tar.gz").split(" ")[0]
    if localmd5 == remotemd5:
        print("MD5 check success...")
    else:
        print("MD5 Check Error")


# run file
@task
def run_task():
    with cd("/home/testdemo"):
        run("tar zxvf fabfile.tar.gz")
        run("python fabfile.py")


# execute all task by order
@task
def go():
    compress_local()
    put_task()
    check_task()
    run_task()
