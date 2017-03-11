# sockets

bind = '0.0.0.0:9081'
backlog = 2048

# worker settings

workers = 4
worker_class = 'gevent'
worker_connection = 1000
timeout = 30
keepalive = 3

# Server mechanics
daemon = False

# Logging
errorlog = 'gunicorn.log'
loglevel = 'info'
accesslog = 'access.log'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

# Process naming

proc_name = 'camel'
