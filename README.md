# Tensor test task
Тестирование результатов поиска и картинок.

## Установка зависимостей:
```sh
pip install -r requirements.txt
```
Запуск тестов
```sh
pytest -v --tb=line
```
Запуск тестов с генерацией html отчета
```sh
pytest -v --capture=sys --tb=line --html=report.html
```
Запуск тестирования поиска
```sh
pytest -v --tb=line -m test_position
```
Запуск тестирования картинок
```sh
pytest -v --tb=line -m test_images
```
