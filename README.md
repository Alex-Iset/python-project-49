<a href="https://ru.hexlet.io/">
<p align="center">
    <img src="images/hexlet_logo.png" 
        width="200" 
        height="200">
</p>
</a>

### Hexlet tests, linter and Code Climate status:
[![Actions Status](https://github.com/Alex-Iset/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Alex-Iset/python-project-49/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/3f97b97684258233f288/maintainability)](https://codeclimate.com/github/Alex-Iset/python-project-49/maintainability)


## Содержание:
### [1. «Игры разума»](#игры-разума)
* [Калькулятор](#калькулятор)
* [Прогрессия](#прогрессия)
* [Определение четного числа](#определение-четного-числа)
* [Определение наибольшего общего делителя](#определение-наибольшего-общего-делителя)
* [Определение простого числа](#определение-простого-числа)
### [2. Установка (Linux)](#установка-linux)
### [3. Как играть?](#как-играть)


## «Игры разума»:
«Игры разума» — набор из пяти консольных игр, построенных по принципу популярных мобильных приложений 
для прокачки мозга. Каждая игра задает вопросы, на которые нужно дать правильные ответы. 
После трех правильных ответов считается, что игра пройдена. 
Неправильные ответы завершают игру и предлагают пройти ее заново.


### Калькулятор
Арифметические выражения, которые необходимо вычислить

Демонстрация игры «Калькулятор» на примере команды Makefile:
[![asciicast](https://asciinema.org/a/1NCaFlTasarIPKNcgn3lZstTK.svg)](https://asciinema.org/a/1NCaFlTasarIPKNcgn3lZstTK)

### Прогрессия
Поиск пропущенных чисел в последовательности чисел

Демонстрация игры «Прогрессия» на примере команды Makefile:
[![asciicast](https://asciinema.org/a/uER0wJLTaH6GWrqYBowbK1GmB.svg)](https://asciinema.org/a/uER0wJLTaH6GWrqYBowbK1GmB)

### Определение четного числа
Демонстрация игры «Определение четного числа» на примере команды Makefile:
[![asciicast](https://asciinema.org/a/T9ql3NprgTcPp517Es8NUBNwv.svg)](https://asciinema.org/a/T9ql3NprgTcPp517Es8NUBNwv)

### Определение наибольшего общего делителя
Демонстрация игры «Определение наибольшего общего делителя» на примере команды Makefile:
[![asciicast](https://asciinema.org/a/7PG7Rrt1LNijJwIUuA1iGGdfC.svg)](https://asciinema.org/a/7PG7Rrt1LNijJwIUuA1iGGdfC)

### Определение простого числа
Демонстрация игры «Определение простого числа» на примере команды Makefile:
[![asciicast](https://asciinema.org/a/nMDVgnj1M6uzn6BfPMODixuFc.svg)](https://asciinema.org/a/nMDVgnj1M6uzn6BfPMODixuFc)


## Установка (Linux):
1. Установка pipx
```
sudo apt install pipx
```
2. Установка Poetry
```
pipx install poetry
```
3. Клонирование репозитория
```
git clone https://github.com/Alex-Iset/python-project-49.git
```
4. Переход в директорию python-project-49
```
cd python-project-49
```
5. Инициализация python-пакета внутри корневой директории проекта
```
poetry init
```
6. Создание виртуального окружения
```
poetry install
```

## Как играть?
Чтобы начать игру можно использовать скрипты Poetry:
```
poetry run brain-calc
poetry run brain-progression
poetry run brain-even
poetry run brain-gcd
poetry run brain-prime
```
Или команды Makefile:
```
make brain-calc
make brain-progression
make brain-even
make brain-gcd
make brain-prime
```
Есть еще вариант запуска игр через создание дистрибутива и его установки:
```
make build
make package-install
```
Теперь игры можно запускать более короткими командами:
```
brain-calc
brain-progression
brain-even
brain-gcd
brain-prime
```