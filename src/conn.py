# -*- coding:utf-8 -*-

def save_ip(rds, ip):
    key = 'local_ip_address'
    rds.hset(key, "ip", ip)

def get_ip(rds):
    key = 'local_ip_address'
    exists = rds.exists(key)
    if not exists:
        return "0"
    ip = rds.hget(key, "ip")
    return ip