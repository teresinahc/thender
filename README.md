# thender
App Tinder-like de candidatos à eleição 2016

---
Como executar?
---
1. Criar e ativar um [ambiente virtual](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
    * `mkvirtualenv thender` para criar um virtualenv chamado thender
    * `workon thender` para ativar o virtualenv sempre que for trabalhar no projeto

2. Instalar as dependências
    * `pip install -r requirements.txt`

3. Criar um arquivo chamado `settings.ini` na pasta sfd com o seguinte conteúdo:
```
[settings]

DATABASE_URL = postgresql://user:password@host:port/db_name
DEBUG = True
SECRET_KEY = a-really-random-secret-key

```

4. Depois de criado o banco de dados (manualmente), crie as tabelas
    * `python manage.py migrate`

5. Iniciar o servidor web
    * `python manage.py runserver`
