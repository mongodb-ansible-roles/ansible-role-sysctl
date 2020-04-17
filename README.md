Ansible role for sysctl
==================================

Linux Kernel Parameters

Use this role to set linux kernel parameters.

[![GitHub Actions](https://github.com/mongodb-ansible-roles/ansible-role-sysctl/workflows/Molecule%20Test/badge.svg)](https://github.com/mongodb-ansible-roles/ansible-role-sysctl/actions?query=workflow%3A%22Molecule+Test%22)
[![GitHub Actions](https://github.com/mongodb-ansible-roles/ansible-role-sysctl/workflows/Release/badge.svg)](https://github.com/mongodb-ansible-roles/ansible-role-sysctl/actions?query=workflow%3A%22Molecule+Test%22)

Requirements
------------
None

Role Variables
--------------

| Name | Description | Type | Default | Required |
|------|-------------|:----:|:-------:|:--------:|
| `kernel_params` | List of kernel parameters and values to set | list | - kernel_param_name: net.ipv4.tcp_fastopen<br>kernel_param_value: 3 | yes |


Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: all
  roles:
    - role: ansible-role-sysctl 
      vars:
        kernel_params:
          - kernel_param_name: net.ipv4.tcp_fastopen
            kernel_param_value: 3
          - kernel_param_name: net.ipv4.tcp_max_syn_backlog
            kernel_param_value: 8192
```

License
-------

[Apache License](LICENSE)
