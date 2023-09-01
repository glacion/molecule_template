def test_molecule_executable(host):
    res = host.run("/tmp/molecule_template/.venv/bin/molecule --version")
    assert res.succeeded
