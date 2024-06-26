#!/usr/bin/python3

"""
Wrap of gdcm application
"""

import os
import subprocess
import sys

import gdcm


def main():
    path = os.path.dirname(gdcm.__file__)
    command = [os.path.join(path, "_gdcm", os.path.basename(sys.argv[0]))]
    command.extend(sys.argv[1:])
    subprocess.call(command)


if __name__ == "__main__":
    main()
