#!/usr/bin/env python
#
# This script should be called with a list, one per line
# of role names that should be registered in .travis.yml
#

from fileinput import input
from sys import stdin

BEGIN = 1
UNPRINTED = 2
PRINTED = 3
END = 4
state = 1
for line in input([".travis.yml"]):
    if line.startswith("### GENERATED ###"):
        state += 1
        print line,
    elif state in (BEGIN, END):
        print line,
    elif state == UNPRINTED:
        state += 1
        roles = stdin.read().strip().split("\n")
        print "env:"
        for role in roles:
            if role.startswith("ansible-role"):
                role = role[13:]
            print "- ROLE=%s" % role
