# Проект "Simple votings"

[Русская версия](#russian-version) | [English Version](#english-version)

<a id="russian-version"></a>
## Русская версия

### Цель
Предоставить пользователю сервис, на котором можно быстро создать голосование и собрать мнения пользователей касательно какого-либо вопроса.

### Технологический стек:
- Python 3.12
- Django 5.1+
- SQLite

### Сам проект на сервере - https://wisetree228.pythonanywhere.com/

### Инструкция по настройке проекта для локального запуска:
1. Склонировать проект.
2. Открыть проект в PyCharm с настройками по умолчанию.
3. Создать виртуальное окружение (через settings -> project "simple votings" -> project interpreter).
4. Открыть терминал в PyCharm, проверить, что виртуальное окружение активировано.
5. Обновить pip:
    ```
    pip install --upgrade pip
    ```

6. Установить в виртуальное окружение необходимые пакеты: 
    ```
    pip install -r requirements.txt
    ```

7. Создать уникальный ключ приложения.  
   Генерация делается в консоли Python при помощи команд:
    ```
    python manage.py shell -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
    ```

   Далее полученное значение подставляется в соответствующую переменную.  
   Внимание! Без выполнения этого пункта никакие команды далее не запустятся.

8. Синхронизировать структуру базы данных с моделями: 
    ```
    python manage.py migrate
    ```

9. Запустите проект:
   ```commandline
   python manage.py runserver
   ```

## Генерация документации
1) Перейдите в папку docs (```cd docs```).
2) Выполните команду 
    ```
    make html
    ```
    (если не сработало, то ```.\make html```).

3) Теперь, когда документация сгенерирована, откройте в браузере файл, который располагается по адресу ```docs/build/html/index.html```.

---

<a id="english-version"></a>
## English Version

### Purpose
To provide a service where users can quickly create a voting poll and gather opinions on a specific question.

### Technology Stack:
- Python 3.12
- Django 5.1+
- SQLite

### The project hosts on - https://wisetree228.pythonanywhere.com/

### Setup Instructions:
1. Clone the project.
2. Open the project in PyCharm with default settings.
3. Create a virtual environment (via settings -> project "simple votings" -> project interpreter).
4. Open the terminal in PyCharm and check that the virtual environment is activated.
5. Upgrade pip:
    ```
    pip install --upgrade pip
    ```

6. Install necessary packages in the virtual environment: 
    ```
    pip install -r requirements.txt
    ```

7. Generate a unique application key.  
   This can be done in the Python console with the following command:
    ```
    python manage.py shell -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
    ```

   The obtained value should then be placed into the corresponding variable.  
   Note! Without completing this step, no further commands will execute.

8. Synchronize the database structure with the models: 
    ```
    python manage.py migrate
    ```
9. Run the project:
   ```commandline
   python manage.py runserver
   ```

## Documentation Generation
1) Navigate to the docs folder (```cd docs```).
2) Execute the command 
    ```
    make html
    ```
    (if it does not work, try ```.\make html```).

3) Now that the documentation has been generated, open the file located at ```docs/build/html/index.html``` in a browser.
