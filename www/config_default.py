#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Default configurations.
'''


configs = {
    'debug': True,
    # 'db': {
    #     'host': '127.0.0.1',
    #     'port': 3306,
    #     'user': 'root',
    #     'password': 'xx',
    #     'db': 'awesome'
    # },
    'db': {
        'host': 'awsblog.cuqtmsbllwin.us-east-1.rds.amazonaws.com',
        'port': 3306,
        'user': 'Draftbk',
        'password': 'xx',
        'db': 'awesome'
    },
    'session': {
        'secret': 'Awesome'
    }
}