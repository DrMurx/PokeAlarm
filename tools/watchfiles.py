#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Standard Library Imports
import os
import sys
# 3rd Party Imports
import configargparse

def parse_unicode(bytestring):
    decoded_string = bytestring.decode(sys.getfilesystemencoding())
    return decoded_string

default_config_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config/config.ini'))

# Set the default config files up
config_files = [default_config_file]
if '-cf' in sys.argv or '--config' in sys.argv:
    config_files = []
parser = configargparse.ArgParser(default_config_files=config_files)
parser.add_argument(
    '-cf', '--config', is_config_file=True, help='Configuration file')

parser.add_argument(
    '-f', '--filters', type=parse_unicode, action='append',
    default=['filters.json'],
    help='Filters configuration file. default: filters.json')
parser.add_argument(
    '-a', '--alarms', type=parse_unicode, action='append',
    default=['alarms.json'],
    help='Alarms configuration file. default: alarms.json')
parser.add_argument(
    '-r', '--rules', type=parse_unicode, action='append',
    default=[None],
    help='Rules configuration file. default: None')
parser.add_argument(
    '-gf', '--geofences', type=parse_unicode,
    action='append', default=[None],
    help='Alarms configuration file. default: None')

args, _ = parser.parse_known_args()

for arg in [args.filters, args.alarms, args.rules, args.geofences]:
    if len(arg) > 1:  # Remove defaults from the list
        arg.pop(0)

#all_files = list(filter(None, args.filters + args.alarms + args.rules + args.geofences))
all_files = args.filters + args.alarms + args.rules + args.geofences

print(" ".join(all_files))
