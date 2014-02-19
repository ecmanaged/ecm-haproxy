#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ecm_haproxy import ECMHAProxy

HAPROXY_CONFIG = '/etc/haproxy/haproxy_build.cfg'

ECM_TEST = {
    'listeners': [
        'HTTP::80::HTTP::80', 'TCP::443::TCP::443'
    ],
    'backends': [
        {'uuid': '62.97.115.10'}, {'uuid2': '62.97.115.12'}
    ],
    'health': {
        'timeout': 5,
        'threshold': 2,
        'interval': 10,
        'check': 'HTTP::80::/check.php'
    }
}

ha_config = ECMHAProxy(ECM_TEST)

print ha_config.show(as_json=True)

if ha_config.valid():
    ha_config.write(HAPROXY_CONFIG)
else:
    raise Exception('Invalid configuration')

print ha_config.read(HAPROXY_CONFIG, as_json=True)
