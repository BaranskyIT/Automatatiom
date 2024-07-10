import pytest
from string_utils import StringUtils

# Создаем экземпляр класса StringUtils для использования в тестах
utils = StringUtils()

def test_capitalize():
    # Позитивный тест
    assert utils.capitilize("example") == "Example"
    # Негативный тест
    assert utils.capitilize("") == ""

def test_trim():
    # Позитивный тест
    assert utils.trim("   example") == "example"
    # Негативный тест
    assert utils.trim("   ") == ""

def test_to_list():
    # Позитивный тест
    assert utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]
    # Негативный тест
    assert utils.to_list("") == []

def test_contains():
    # Позитивный тест
    assert utils.contains("Example", "E") == True
    # Негативный тест
    assert utils.contains("Example", "Z") == False

def test_delete_symbol():
    # Позитивный тест
    assert utils.delete_symbol("Example", "m") == "Exaple"
    # Негативный тест
    assert utils.delete_symbol("Example", "ple") == "Exam"

def test_starts_with():
    # Позитивный тест
    assert utils.starts_with("Example", "E") == True
    # Негативный тест
    assert utils.starts_with("Example", "x") == False

def test_end_with():
    # Позитивный тест
    assert utils.end_with("Example", "e") == True
    # Негативный тест
    assert utils.end_with("Example", "m") == False

def test_is_empty():
    # Позитивный тест
    assert utils.is_empty("") == True
    # Негативный тест
    assert utils.is_empty(" ") == True
    assert utils.is_empty("Example") == False

def test_list_to_string():
    # Позитивный тест
    assert utils.list_to_string([1,2,3,4]) == "1, 2, 3, 4"
    assert utils.list_to_string(["Test", "Case"]) == "Test, Case"
    # Негативный тест
    assert utils.list_to_string(["Test", "Case"], "-") == "Test-Case"
    assert utils.list_to_string([]) == ""

if __name__ == "__main__":
    pytest.main()
