# Задание №7
# Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# Каждая группа включает файлы с несколькими расширениями.
# В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

import os

import Task6 as tsk
from pathlib import Path


def sort_files(path: Path | str, groups: dict[Path, list[str]]=None) -> None:
    if groups is None:
        groups = {
            Path("video"): ['avi', 'mkv'],
            Path("pic"): ['png', 'jpg'],
            Path("music"): ['mp3']
        }

    if isinstance(path, str):
        path = Path(path)

    os.chdir(path)
    for target_dir, ext_list in groups.items():
        if not target_dir.is_dir():
            target_dir.mkdir()
        for file in list(os.walk(Path.cwd()))[0][-1]:
            if file.split('.')[-1] in ext_list:
                os.replace(file, os.path.join(target_dir, file))


tsk.gen_files(r'C:\Users\user\PycharmProjects\GBTester\PySummer\S7_11_06\test_task7', avi=2, mkv=1, png=2, mp3=2, jpg=2)
variable = r'C:\Users\user\PycharmProjects\GBTester\PySummer\S7_11_06\test_task7'
sort_files(variable)