from testinfra.modules.service import Service


def test_ssh_service(host):
    it: Service = host.service("ssh")

    assert it.is_valid
    assert it.is_enabled
