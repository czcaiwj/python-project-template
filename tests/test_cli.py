import shutil
import subprocess
import sys
import sysconfig

import pytest

from python_project_template import main


def test_main(capsys: pytest.CaptureFixture[str]) -> None:
    assert main() is None
    captured = capsys.readouterr()
    assert captured.out == "Hello from python-project-template!\n"
    assert captured.err == ""


@pytest.mark.parametrize("entrypoint", ["module", "console_script"])
def test_entrypoint(entrypoint: str) -> None:
    if entrypoint == "module":
        command = [sys.executable, "-m", "python_project_template"]
    else:
        script = shutil.which("python-project-template", path=sysconfig.get_path("scripts"))
        assert script is not None, "The console script must be installed in the test environment"
        command = [script]

    result = subprocess.run(command, capture_output=True, text=True, check=False, timeout=10)

    assert result.returncode == 0, result.stderr
    assert result.stdout == "Hello from python-project-template!\n"
    assert result.stderr == ""
