#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack."""

from fabric.api import *
import time
from os import path, stat
def do_pack():

    try:
        stat("versions")
    except:
        local("mkdir versions")
    try:
        time_tuple = time.localtime()
        file_path = "versions/web_static_" + \
            time.strftime("%Y%m%d%H%M%S", time_tuple) + ".tgz"
        print("Packing web_static to " + file_path)
        local("tar -cvzf " + file_path + " web_static")
        size = path.getsize(file_path)
        print("web_static packed: " + file_path + " -> " + str(size) + "Bytes")
        return file_path
    except:
        return None
    
