from testinfra.modules.file import File


def test_molecule_executable(host):
    it: File = host.file("/tmp/molecule_template/pyproject.toml")

    assert it.exists
