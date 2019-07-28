import pytest

from solutions.{{cookiecutter.file_name}} import {{cookiecutter.class_name}}PartA


class Test{{cookiecutter.class_name}}PartA:
    @pytest.mark.parametrize(("input_data", "expected_result"), [("", ""), ("", "")])
    def test_day05a_solve(self, input_data, expected_result):
        solution = {{cookiecutter.class_name}}PartA()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day05a_data(self):
        """ Result we got when we did the real solution """
        solution = {{cookiecutter.class_name}}PartA()
        res = solution("{{cookiecutter.file_name}}PartA/{{cookiecutter.directory_name}}.txt")
        assert res == 0
