#!/usr/bin/env python3

import sys

from gyro_listener import GyroListener

if __name__ == "__main__":
    try:
        if len(sys.argv) != 3:
            raise RuntimeError
        int(sys.argv[2])
    except (RuntimeError, ValueError):
        print("Usage: main.py <ip-address> <port>")
        exit(1)

    gl = GyroListener(sys.argv[1], int(sys.argv[2]), conn_limit = 1)
    gl.start()
