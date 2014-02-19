#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Convert a ECM Balancer hash to haproxy configuration file
# This file is just for testing purposes

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

# Show configuration
print ha_config.show(as_json=True)

# Write new configuraion if is valid
if ha_config.valid():
    ha_config.write(HAPROXY_CONFIG)
else:
    raise Exception('Invalid configuration')

# Write ECM json hash from final configuration file
print ha_config.read(HAPROXY_CONFIG, as_json=True)
