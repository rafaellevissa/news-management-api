# 📰 JOTA Backend API

Este projeto é uma API RESTful desenvolvida com Django e Django REST Framework para gerenciamento de notícias. 

## 🚀 Tecnologias Utilizadas

- Python 3.11+
- Django 4.x
- Django REST Framework
- PostgreSQL
- JWT (via `djangorestframework-simplejwt`)
- Docker + Docker Compose
- Swagger (via `drf-spectacular`)


## ⚠️ Pendências

Ainda não foi implementado:
- ✅ Testes automatizados (unitários e de integração)
- ✅ Pipeline de CI/CD (GitHub Actions)
- ✅ Seed de dados com usuário inicial/admin criado automaticamente

## 🛠️ Como Executar Localmente

> É necessário ter o **Docker** e o **Docker Compose** instalados.

```bash
docker compose up
```

A aplicação estará disponível em `http://localhost:8000`.

A documentação interativa da API pode ser acessada em:

```
http://localhost:8000/swagger/
```

## ✅ Próximos Passos

- Criar fixtures/seeds para cadastrar usuários iniciais e planos
- Configurar GitHub Actions para rodar testes e deploy contínuo
- Escrever testes com `pytest` para cobertura das principais regras de negócio
- Modularizar serviços (ex: separação de domínio de usuários e notícias)
- Pensar na separação de microsserviços em um segundo momento
