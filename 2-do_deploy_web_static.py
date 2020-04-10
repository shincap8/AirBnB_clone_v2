#!/usr/bin/python3
"""Fabric script (based on the file 1-pack_web_static.py) that
distributes an archive to your web servers, using the function do_deploy:"""

from fabric.api import *
import time
from os import path

env.hosts = ['35.237.41.190', '3.90.183.111']


def do_deploy(archive_path):
    if path.isfile(archive_path) is False:
        return False
    try:
        name = archive_path[9:-4]
        print(name)
        put(archive_path, "/tmp/" + name + ".tgz")
        host_path = "/data/web_static/releases/" + name + "/"
        run("mkdir -p " + host_path)
        run("tar -xzf /tmp/" + name + ".tgz -C " + host_path)
        run("rm /tmp/" + name + ".tgz")
        run("mv /data/web_static/releases/" + name +
            "/web_static/* " + host_path)
        run("rm -rf " + host_path + "web_static")
        run("rm -rf /data/web_static/current")
        run("ln -s " + host_path + " /data/web_static/current")
        print("New version deployed!")
        return True
    except:
        return False
