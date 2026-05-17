### Hexlet tests and linter status:
[![Actions Status](https://github.com/TaRgITay008/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/TaRgITay008/python-project-52/actions)

[![Quality Gate Status](https://img.shields.io/badge/quality%20gate-passing-brightgreen)](https://sonarcloud.io/summary/new_code?id=TaRgITay008_python-project-52)

[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)](https://sonarcloud.io/summary/new_code?id=TaRgITay008_python-project-52)

# Task Manager

Task Manager — система управления задачами, подобная Redmine. Позволяет создавать задачи, назначать исполнителей, управлять статусами и метками.

## Деплой

Проект развёрнут на Render: [https://hexlet-code-i44q.onrender.com](https://hexlet-code-i44q.onrender.com)

## Установка и запуск

```bash
# Клонировать репозиторий
git clone https://github.com/TaRgITay008/python-project-52.git
cd python-project-52

# Установить зависимости через uv
uv sync

# Применить миграции
uv run python manage.py migrate

# Запустить сервер
uv run python manage.py runserver


# Force rebuild - Sat May 16 23:46:13 MSK 2026
