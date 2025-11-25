# Webhook Events Collector

Este projeto é uma API simples em **Python + Flask** para receber webhooks, armazenar os eventos em um volume persistente e disponibilizá-los por meio de uma rota `/events`.

Ideal para testes, debugging ou demonstrações de pipelines CI/CD, GitOps, GitHub/GitLab webhooks e integrações diversas.

---

## 🚀 Funcionalidades

- Recebe webhooks via `POST /webhook`
- Persiste eventos em **SQLite**, armazenado em `/data/events.db`
- Rota `GET /events` retorna todos os eventos
- Ordem dos eventos: mais recentes primeiro
- Suporte a CORS
- Pode ser executado localmente ou em containers (Kubernetes-friendly)

---

## 🗂 Estrutura
