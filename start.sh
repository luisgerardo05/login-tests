#!/bin/bash

# locust -f control.py --host http://localhost.com:5000 --headless -u 5 -r 5 --run-time 30s --stop-timeout 10 --exit-code-on-error 1

# locust -f login.py --host http://localhost.com:5000 --headless -u 5 -r 5 --run-time 30s --stop-timeout 10 --exit-code-on-error 1

locust -f register.py --host http://localhost.com:5000 --headless -u 5 -r 5 --run-time 30s --stop-timeout 10 --exit-code-on-error 1
