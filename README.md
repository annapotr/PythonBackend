# PythonBackend

Чтобы запустить тесты, напишите: `python3 -m pytest`

Чтобы заапустить нагрузочные тесты, напишите: `locust -f tests/locustfile.py`

[Отчет нагрузочного тестирования](Отчет%20нагрузочного%20тестирования.pages)

GraphQL:
Чтобы запустить, напишите: `uvicorn main:app --reload`

```{
  me{
    id
    name
    disease
    symptoms{
      id
      name
    }
  }
  myFriend{
    id
    name
    disease
    symptoms{
      id
      name
    }
  }
  myPet{
    id
    name
    disease
    symptoms{
      id
      name
    }
  }
}
```
[Схема микросервисов и инструкция по расширению микросервисов](Diagram.drawio.png)

Запустить сервес rendering: `uvicorn project.servers.rendering.main:app --reload`

Запустить сервес user: `uvicorn project.servers.user.main:app --reload --port 8002`

Запустить сервес working_with_image: `uvicorn project.servers.working_with_image.main:app --reload --port 8001`

[Сравнение СУБД](СравнениеСУБД.pages)

## Алгоритм развертывания: 

1. Скачайте MySQL
2. Запустите MySQL Workbench 
3. CREATE DATABASE mybd
4. Впишите свои данные в `project/servers/database/database.py`
`create_engine("mysql+pymysql://имя_тут:пароль_тут@localhost:порт_тут/mybd")`
   
Запустить тесты базы данных:
`python -m pytest project/tests/test_database.py`