#!/usr/bin/env python
"""
Скрипт для просмотра данных из базы данных SQLite
Использование: python view_db.py
"""
import os
import sys
import django

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'invoicely.settings')
django.setup()

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

def view_users():
    """Показать всех пользователей"""
    print("\n" + "="*50)
    print("ПОЛЬЗОВАТЕЛИ В БАЗЕ ДАННЫХ")
    print("="*50)

    users = User.objects.all()

    if not users.exists():
        print("Пользователей не найдено!")
        return

    for user in users:
        print(f"\nID: {user.id}")
        print(f"Username: {user.username}")
        print(f"Email: {user.email}")
        print(f"Имя: {user.first_name}")
        print(f"Фамилия: {user.last_name}")
        print(f"Активен: {user.is_active}")
        print(f"Суперпользователь: {user.is_superuser}")
        print(f"Дата регистрации: {user.date_joined}")

        # Проверяем наличие токена
        try:
            token = Token.objects.get(user=user)
            print(f"Token: {token.key}")
        except Token.DoesNotExist:
            print("Token: не создан")

        print("-" * 50)

def view_tokens():
    """Показать все токены"""
    print("\n" + "="*50)
    print("ТОКЕНЫ В БАЗЕ ДАННЫХ")
    print("="*50)

    tokens = Token.objects.all()

    if not tokens.exists():
        print("Токенов не найдено!")
        return

    for token in tokens:
        print(f"\nПользователь: {token.user.username}")
        print(f"Token: {token.key}")
        print(f"Создан: {token.created}")
        print("-" * 50)

if __name__ == '__main__':
    print("\nПросмотр базы данных Django\n")

    view_users()
    view_tokens()

    print("\n" + "="*50)
    print("Для просмотра через Django admin:")
    print("1. Создайте суперпользователя: python manage.py createsuperuser")
    print("2. Запустите сервер: python manage.py runserver")
    print("3. Откройте: http://127.0.0.1:8000/admin")
    print("="*50 + "\n")


