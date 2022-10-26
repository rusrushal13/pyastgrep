import os
from pathlib import Path

from pyastgrep.search import get_files_to_search
from tests.utils import chdir

DIR = os.path.dirname(__file__) + "/examples/test_ignores"


def test_default_ignores():
    with chdir(DIR):
        files = list(get_files_to_search(["."]))

    for p in ["__init__.py", "not_ignored.py", "subdir/not_ignored.py"]:
        assert Path(p) in files

    # `.custom_hidden` should be ignored by default
    for p in [".custom_hidden/__init__.py", ".custom_hidden/should_be_ignored.py", "subdir/.custom_hidden/__init__.py"]:
        assert Path(p) not in files

    # node_modules is in this repo's .gitignore
    for p in ["node_modules/__init__.py", "node_modules/should_be_ignored.py"]:
        assert Path(p) not in files


def test_override_on_cli():
    """
    Directories specified on command line should always be searched.
    """
    with chdir(DIR):
        files = list(get_files_to_search(["node_modules"]))

    for p in ["node_modules/__init__.py", "node_modules/should_be_ignored.py"]:
        assert Path(p) in files
