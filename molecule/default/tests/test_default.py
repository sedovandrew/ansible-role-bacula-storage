import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_bacula_storage_is_installed(host):
    assert host.package("bacula-storage").is_installed


def test_bacula_storage_is_running(host):
    host.service("baculd-sd").is_running


def test_bacula_storage_is_enabled(host):
    host.service("bacula-sd").is_enabled


def test_bacula_storage_listen_port(host):
    host.socket("tcp://0.0.0.0:9103")
