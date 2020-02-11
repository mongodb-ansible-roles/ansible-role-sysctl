import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_host(host):
    assert host.file("/etc/hosts").exists


def test_sysctl_conf(host):
    assert host.file("/etc/sysctl.conf").contains("net.ipv4.tcp_fastopen=3")
