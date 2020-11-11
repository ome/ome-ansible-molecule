# Molecule action

A GitHub action to tests your [Ansible](https://www.ansible.com/) role using [Molecule](https://molecule.readthedocs.io/en/stable/).

## Requirements

This action expects the following (default Ansible role) structure:
```
.
├── defaults
│   └── main.yml
├── handlers
│   └── main.yml
├── meta
│   └── main.yml
├── molecule
│   └── default
│       ├── molecule.yml
│       ├── playbook.yml
│       └── prepare.yml
├── requirements.yml
├── tasks
│   └── main.yml
├── tox.ini # OPTIONAL
└── vars
    └── main.yml
```

If you are missing the `molecule` directory, please have a look at this [skeleton role](https://github.com/robertdebock/ansible-role-skeleton) or one of the many examples listed on [my website](https://robertdebock.nl/).

When `tox.ini` is found, [tox](https://tox.readthedocs.io/en/latest/) is used to test the role.

## Inputs

### `namespace`

The Docker Hub namespace where the image is in. Default '"robertdebock"'.

### `image`

The image you want to run on. Default '"fedora"'.

### `tag`

The tag of the container image to use. Default '"latest"'.

### `options`

The options to pass to `tox`. For example `parallel`. Default '""'. (empty)

## Example usage

Here is a default configuration that tests your role on `namespace: robertdebock`, `image: fedora`, `tag: latest`.

```yaml
---
on:
  - push

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: checkout
        uses: actions/checkout@v2
        with:
          path: "${{ github.repository }}"
      - name: molecule
        uses: robertdebock/molecule-action@1.2.2
```

NOTE: the `checkout` action needs to place the file in `${{ github.repository }}` in order for Molecule to find your role.

If you want to test your role against multiple distributions, you can use this pattern:

```yaml
---
name: CI

on:
  - push

jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        image:
          - alpine
          - amazonlinux
          - debian
          - centos
          - fedora
          - opensuse
          - ubuntu
    steps:
      - name: checkout
        uses: actions/checkout@v2
        with:
          path: "${{ github.repository }}"
      - name: molecule
        uses: robertdebock/molecule-action@1.2.2
        with:
          image: "${{ matrix.image }}"
          options: parallel
```
