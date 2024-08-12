import pytest
from lesson8.Pages.TodoMain import Task

def test_todo():
    quest = Task()

    list = quest.get_list()
    assert list.status_code == 200

    params = {"title": "Автоматизация Python", 'completed': False}
    task = quest.create(params)
    assert task is not None

    params = {"title": "Автоматизация Python работает"}
    rename_task = quest.rename(task, params)
    assert rename_task.json()['title'] == "Автоматизация Python работает"

    info = quest.info(task)
    assert info.json()['title'] == "Автоматизация Python работает"
    assert info.json()['id'] == task

    params = {'completed': False}
    status_false = quest.change_status(task, params)
    assert status_false == False

    deleted = quest.delete(task)
    assert deleted == 200
