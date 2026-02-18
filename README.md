📌 Documento de Especificação
Sistema de Favoritos e Coleções de Ofertas

1️⃣ Visão Geral
📖 Descrição
Sistema backend desenvolvido em Python + Django + Django Rest Framework que permite aos usuários:
Salvar ofertas/produtos como favoritos
Organizar favoritos em coleções
Seguir outros usuários
Visualizar feed personalizado
Receber notificações de interações
O sistema é inspirado no modelo social de curadoria de conteúdo como Pinterest.

2️⃣ Objetivos do Projeto
🎯 Objetivo Principal
Criar uma API escalável que permite gerenciamento de favoritos com comportamento social.
🎯 Objetivos Técnicos
Exercitar modelagem relacional
Trabalhar com relacionamentos complexos
Implementar feed escalável
Aplicar cache com Redis
Garantir performance com alto volume de usuários
Trabalhar com concorrência e integridade de dados

3️⃣ Escopo Funcional
👤 Usuários
Cadastro
Login
Perfil público
Perfil privado (opcional)

🔖 Ofertas
Criar oferta
Editar oferta
Excluir oferta
Visualizar oferta
Contador de favoritos

📁 Coleções
Criar coleção
Editar nome
Tornar pública/privada
Listar coleções do usuário
Adicionar/remover oferta da coleção

❤️ Favoritos
Favoritar oferta
Remover favorito
Listar favoritos do usuário
Ver quem favoritou uma oferta

👥 Sistema de Seguidores
Seguir usuário
Deixar de seguir
Listar seguidores
Listar quem está seguindo

📰 Feed Personalizado
Exibir:
Ofertas salvas por usuários seguidos
Novas ofertas criadas por usuários seguidos
Ordenado por:
Data
Score de engajamento (opcional)

🔔 Notificações
Gerar notificação quando:
Alguém seguir o usuário
Alguém favoritar sua oferta
Funcionalidades:
Listar notificações
Marcar como lida

4️⃣ Requisitos Não Funcionais
⚡ Performance
Responder requisições de feed em < 300ms
Suportar 1.000 usuários ativos simultâneos
🔐 Segurança
Autenticação JWT
Permissões por usuário
Proteção contra duplicate favorites
📈 Escalabilidade
Cache de feed no Redis
Paginação (se possível utilizar cursor-based)
Índices em campos estratégicos

5️⃣ Arquitetura Técnica
Stack
Python
Django
Django Rest Framework
PostgreSQL
Redis
Celery 
Docker

Arquitetura de Camadas
apps/
  users/
  offers/
  favorites/
  collections/
  social/
  feed/
  notifications/

6️⃣ Modelagem de Dados
User
Modelo padrão do Django (ou customizado)

Offer
Campos principais:
id
title
description
price
image_url
created_by (FK User)
favorites_count
created_at

Collection
Campos:
id
name
user (FK User)
is_public
created_at

Favorite
Campos:
id
user (FK User)
offer (FK Offer)
collection (FK Collection - opcional)
created_at
Constraint:
unique(user, offer)

Follow
Campos:
id
follower (FK User)
following (FK User)
created_at
Constraint:
unique(follower, following)

Feed
Campos:
id
user (quem vê o feed)
actor (quem gerou ação)
offer
action_type (FAVORITE, CREATED)
created_at

Notification
Campos:
id
user (quem recebe)
actor (quem gerou)
type
is_read
created_at

7️⃣ Regras de Negócio
Usuário não pode favoritar a mesma oferta duas vezes
Usuário não pode seguir a si mesmo
Usuário não pode ver coleções privadas de outros
Ao deletar oferta:
Remover favoritos associados
Atualizar feed
favorites_count deve sempre refletir valor real

8️⃣ Fluxos Importantes
🔁 Fluxo: Favoritar Oferta
Validar autenticação
Verificar se já existe favorito
Criar Favorite
Incrementar favorites_count
Criar item no feed dos seguidores
Criar notificação para dono da oferta

🔁 Fluxo: Seguir Usuário
Validar autenticação
Verificar se já segue
Criar Follow
Criar notificação

9️⃣ Estratégia de Feed
Estratégia Recomendada: Feed Pré-calculado
Quando ação acontece:
Buscar seguidores do ator
Criar entradas de feed para cada seguidor
Cachear lista no Redis
Benefício:
Feed extremamente rápido

🔟 Estratégia de Performance
select_related em Offer → created_by
prefetch_related em followers
Índices:
(user, created_at) no Feed
(offer, created_at) em Favorite
(follower, following) em Follow
Cache:
Feed por usuário
Ofertas populares
Perfil público

1️⃣1️⃣ Endpoints da API
Autenticação
POST /auth/login
POST /auth/register

Ofertas
POST /offers/
GET /offers/
GET /offers/{id}/

Favoritos
POST /offers/{id}/favorite/
DELETE /offers/{id}/favorite/
GET /users/{id}/favorites/

Coleções
POST /collections/
GET /collections/
PATCH /collections/{id}/

Social
POST /users/{id}/follow/
DELETE /users/{id}/follow/
GET /users/{id}/followers/

Feed
GET /feed/

Notificações
GET /notifications/
PATCH /notifications/{id}/read/

1️⃣2️⃣ Possíveis Evoluções Futuras
Sistema de ranking (trending)
Algoritmo de recomendação
Sistema de comentários
Sistema de badges
Sistema premium
Analytics por usuário

1️⃣3️⃣ Critérios de Aceitação
✔ Todas as operações devem respeitar autenticação
✔ Não deve haver inconsistência no contador de favoritos
✔ Feed deve ser paginado

📌 Resultado Esperado
Uma API social escalável de curadoria de ofertas, inspirada em modelos como Instagram e Pinterest, pronta para:
Portfólio profissional
Base de SaaS
Estudo avançado de arquitetura

