# Тестовое задание для: Python[Django] разработчика

Необходимо разработать backend архитектуру и смоделировать работоспособный `RESTful`-интерфейс, достаточный для использования frontend-разработчиками и администраторами проекта.

Требуется:
1. Построить структуру БД, используя СУБД `PostgreSQL`.
2. Настроить редактирование этих данных в панели администратора `Django`.
3. Написать `RESTful-API` для получения данных из этих моделей
4. Покрыть `unit`-тестами (использование pytest будет плюсом).
5. Проект развернуть в `Docker`.
6. `API` закрыть токеном.

Требуется наличие следующих сущностей:
1. Район города
2. Категория
3. Сеть предприятий
4. Предприятие:
Принадлежит одной из сети предприятий
* имеет принадлежность к нескольким районам города, может быть представлена сразу в нескольких;
* имеет список предоставляемых услуг\товаров с ценами.
5. Услуга\товар:
* может продаваться в одном или нескольких предприятиях в сети
* цена может отличаться в зависимости от предприятия

Требуются следующие ресурсы API:
1. Список предприятий - с условием заранее выбранного района:
* url - `/organizations/<district_id>/`;
* фильтры - по категории товаров\услуг в этом предприятии
* поиск по названию товара\услуги (реализация неточного поиска будет плюсом).
2. Детальная информация по заведению
3. Добавление товара/услуги
4. Детальная информация по товару\услуге

Стек технологий - `Django`, `DjangoRestFramework`, `git`, `Docker`.
