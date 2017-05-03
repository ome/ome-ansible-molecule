#!/usr/bin/env python
#
# This script should be called with a list, one per line
# of role names that should be registered in .travis.yml
# (e.g. from ./repos.sh)
#

import re
import sys

TAG = "###GENERATED###"

with open(".travis.yml", "r") as fin:
    txt = fin.read()

roles = sys.stdin.read().strip().split("\n")
replacement = "%s\nenv:\n" % TAG
for role in roles:
    if role.startswith("ansible-role"):
        role = role[13:]
    replacement += "- ROLE=%s\n" % role
replacement += "%s" % TAG
print re.sub("%s.*?%s" % (TAG, TAG), txt, replacement, flags=re.DOTALL),
