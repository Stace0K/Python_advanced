# Задание №6
#  На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень).
# Напишите 3-7 тестов pytest для данного проекта.
# Используйте фикстуры.

import json
import pytest


@pytest.fixture
def set_up_data():
    users = {
        User(name="Sasha", user_id="2", user_level="1"),
        User(name="Masha", user_id="1", user_level="2"),
        User(name="Dasha", user_id="3", user_level="5"),
        User(name="Glasha", user_id="4", user_level="7")
    }
    return users


@pytest.fixture
def success_login():
    return User(name="Sasha", user_id="2", user_level="1")


@pytest.fixture
def new_user():
    return User(name="newUser", user_id="5", user_level="3")


def test_load(set_up_data):
    file = 'users.json'
    project1 = Project()
    result = project1.load_json(file)
    assert set_up_data == result


def test_login(success_login):
    file = 'users.json'
    project1 = Project()
    project1.load_json(file)
    result = project1.login(name="Sasha", id="2")
    assert success_login == result


def test_no_login():
    file = 'users.json'
    project1 = Project()
    project1.load_json(file)
    name, id = "qwerty", "0"
    with pytest.raises(AccessError,
                       match=f'Ошибка доступа: Отсутствует пользователь с именем {name} и идентификатором {id}!!'):
        project1.login("qwerty", "0")


def test_add_user(new_user):
    file = 'users.json'
    project1 = Project()
    project1.load_json(file)
    project1.login(name="Sasha", id="2")
    result = project1.add_user("newUser", "5", "3")
    assert new_user == result


def test_not_add_user():
    file = 'users.json'
    project1 = Project()
    project1.load_json(file)
    project1.login(name="Dasha", id="3")
    name, id, level = "qwerty", "5", "1"
    with pytest.raises(
            LevelError,
            match=f'Ошибка уровня: Вы вошли как - {project1.user.name} и ограничены уровнем {project1.user.user_level}.\n'
                  f' Нельзя добавить пользователя - {name} с уровнем {level}!!!\n'
                  f'Наказание РАСТРЕЛЛ!!'
    ):
        project1.add_user(name, id, level)


class UserException(Exception):
    pass


class LevelError(UserException):
    def __init__(self, user, new_user):
        self.user = user
        self.new_user = new_user

    def __str__(self):
        return (f'Ошибка уровня: Вы вошли как - {self.user.name} и ограничены уровнем {self.user.user_level}.\n'
                f' Нельзя добавить пользователя - {self.new_user.name} с уровнем {self.new_user.user_level}!!!\n'
                f'Наказание РАСТРЕЛЛ!!')


class AccessError(UserException):
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __str__(self):
        return f'Ошибка доступа: Отсутствует пользователь с именем {self.name} и идентификатором {self.id}!!'


class User:
    def __init__(self, name: str, user_id: str, user_level: str):
        self.name = name
        self.user_id = user_id
        self.user_level = user_level

    def __eq__(self, other):
        return self.user_id == other.user_id and self.name == other.name

    def __hash__(self) -> int:
        return hash((self.name, self.user_id))

    def __str__(self):
        return f'{self.name} {self.user_id} {self.user_level}'

    def __repr__(self):
        return f'User({self.name}, {self.user_id}, {self.user_level})'


class Project:
    def __init__(self):
        self.users = set()
        self.user = None

    def login(self, name, id):
        login_user = User(name, id, '0')
        if login_user not in self.users:
            raise AccessError(name, id)

        for cur_user in self.users:
            if login_user == cur_user:
                self.user = cur_user
                return self.user

    def add_user(self, name, id, level):
        new_user = User(name, id, level)
        if int(self.user.user_level) > int(level):
            raise LevelError(self.user, new_user)
        # new_user = User(name, id, level)
        self.users.add(new_user)
        return new_user

    def load_json(self, filename):
        with open(filename, 'r', encoding='utf-8') as f_read:
            data = json.load(f_read)

        for level, users_dict in data.items():
            for id, name in users_dict.items():
                self.users.add(User(name, id, level))
        return self.users


if __name__ == '__main__':
    pytest.main(["-vv"])