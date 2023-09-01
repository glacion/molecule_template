from testinfra.modules.file import File


def test_molecule_executable(host):
    it: File = host.file("/tmp/molecule_template/.venv/bin/molecule")

    assert it.is_executable
