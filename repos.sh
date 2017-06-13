#!/bin/bash
curl -q 'https://api.github.com/users/openmicroscopy/repos?per_page=100' | \
    jq --raw-output '.[] | .name' | grep -E ^ansible-role
