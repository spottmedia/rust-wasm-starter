import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_rustc_installed(host):
    cmd = host.run("rustc --version")
    assert cmd.stderr == ''
    assert 'rustc' in cmd.stdout


def test_cargo_installed(host):
    cmd = host.run("cargo --version")
    assert cmd.stderr == ''
    assert 'cargo' in cmd.stdout


def test_wasm_pack_installed(host):
    cmd = host.run("wasm-pack --version")
    assert cmd.stderr == ''
    assert 'wasm-pack' in cmd.stdout


def test_node_version_ok(host):
    cmd = host.run("node -v")
    assert cmd.stderr == ''
    assert cmd.stdout.rstrip() == 'v10.16.0'


def test_npm_ok(host):
    cmd = host.run("npm -v")
    assert cmd.stdout.rstrip() == '6.9.0'


@pytest.mark.parametrize('port', [
    '80'
])
def test_ports(host, port):
    assert host.socket("tcp://::1:{}".format(port)).is_listening
