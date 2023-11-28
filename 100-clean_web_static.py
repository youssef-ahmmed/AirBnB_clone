#!/usr/bin/python3
"""deletes out-of-date archives"""

from fabric.api import local, run, env
import os


def do_clean(number=0):
    """clean unnecessary files"""
    number = 1 if number == '0' else int(number)
    versions = os.listdir('versions').sort()
    size = len(os.listdir('versions'))
    for file in versions[:size - int(number)]:
        local('rm versions/{:s}'.format(file))

        run('rm -rf /data/web_static/releases/{:s}'.format(file))



salma_list = [1, 2, 2, 4]
salma = 'salma ahmed'

print(salma.partition(' '))