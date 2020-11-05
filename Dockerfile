# This is based on
# https://github.com/robertdebock/docker-github-action-molecule/blob/fc79ec2e0e68500e366f30291056eb68d32e67b8/Dockerfile

# ubuntu:20.04 has Python 3.8 so can't be used
# https://github.com/ome/ome-ansible-molecule/issues/23
FROM ubuntu:18.04

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
WORKDIR /github/workspace

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y -q \
        docker.io \
        python3 \
        python3-pip \
        python3-venv && \
     rm -rf /var/lib/apt/lists/*

ADD LICENSE.txt MANIFEST.in README.rst setup.py /src/
RUN python3 -mvenv /venv && \
    /venv/bin/pip install /src

RUN ln -fs /bin/bash /bin/sh && \
    ln -fs /venv/bin/* /usr/local/bin

ENV RETRIES=2

CMD function retry { counter=0 ; until "$@" ; do exit=$? ; counter=$(($counter + 1)) ; if [ $counter -ge $RETRIES ] ; then return $exit ; fi ; done ; return 0; } ; cd ${GITHUB_REPOSITORY} ; if [ -f tox.ini -a ${command:-test} = test ] ; then retry tox ${options} ; else PY_COLORS=1 ANSIBLE_FORCE_COLOR=1 retry molecule ${command:-test} --scenario-name ${scenario:-default}; fi
