import os.path
import sys

from tests.utils import run_print

DIR = os.path.dirname(__file__) + "/examples/test_xml"


def test_literals():
    # We need a way to distinguish between different literals
    if sys.version_info < (3, 8):
        expr_int = ".//Num"
        expr_string = ".//Str"
    else:
        expr_int = './/Constant[@type="int"]'
        expr_string = './/Constant[@type="str"]'

    output_int = run_print(DIR, expr_int, print_xml=True).stdout
    output_string = run_print(DIR, expr_string, print_xml=True).stdout
    assert "assigned_int" in output_int
    assert "assigned_string" not in output_int

    assert "assigned_int" not in output_string
    assert "assigned_string" in output_string
