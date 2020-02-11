Ansible role for sysctl
==================================

Linux Kernel Parameters

Use this role to set linux kernel parameters.

Currently we are turning on `net.ipv4.tcp_fastopen` on all linux versions with a kernel version higher than 4.11

[![GitHub Actions](https://github.com/mongodb-ansible-roles/ansible-role-sysctl/workflows/Molecule%20Test/badge.svg)](https://github.com/mongodb-ansible-roles/ansible-role-sysctl/actions?query=workflow%3A%22Molecule+Test%22)
[![GitHub Actions](https://github.com/mongodb-ansible-roles/ansible-role-sysctl/workflows/Release/badge.svg)](https://github.com/mongodb-ansible-roles/ansible-role-sysctl/actions?query=workflow%3A%22Molecule+Test%22)

Requirements
------------

None

Role Variables
--------------

| Name | Description | Type | Default | Required |
|------|-------------|:----:|:-------:|:--------:|
| name | desc | type | default | required |

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: all
  roles:
    - role: ansible-role-sysctl
```

License
-------

[Apache License](LICENSE)
