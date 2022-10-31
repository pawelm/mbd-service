build:
	docker compose build

up:
	docker compose up

run_alembic:
	docker compose run api alembic upgrade head

init_db: run_alembic