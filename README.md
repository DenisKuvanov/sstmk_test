# Readme

## Запуск скрипта для проверки доступности сайта и получения номера телефона компании

Этот скрипт на Python позволяет проверить доступность веб-сайта и получить номер телефона компании с его главной страницы. Для выполнения скрипта вам потребуется Python 3 и установленные библиотеки requests, beautifulsoup4 и lxml.

### Шаги для запуска:

1. **Установка Python 3:** Если у вас еще нет Python 3, его можно скачать и установить с официального сайта [python.org](https://www.python.org/).

2. **Установка зависимостей:** Откройте терминал и выполните следующие команды, чтобы установить необходимые библиотеки:

    ```
    pip install requests
    pip install beautifulsoup4
    pip install lxml
    ```

3. **Запуск скрипта:** После установки библиотек откройте терминал, перейдите в каталог со скриптом и выполните следующую команду:

    ```
    python check_site.py
    ```

4. **Результаты:** После запуска скрипта вы увидите результаты его работы в консоли. Если сайт доступен, скрипт выведет IP-адрес сайта и номер телефона компании (если он найден на сайте). Если сайт недоступен, будет выведено соответствующее сообщение.

