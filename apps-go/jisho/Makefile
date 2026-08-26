env_file = ../../.env

build_dir = ./bin
server_build_dir = ./bin/server
exec_build_dir = ./bin/exec

server_dir = ./cmd/server
exec_dir = ./cmd/exec

sql_engine = postgres
sql_migrations_dir = ./sql/migrations

.PHONY: clean
clean: confirm
	@echo "Cleaning build artifacts..."
	@rm -rf ${build_dir}

.PHONY: confirm
confirm:
	@echo -n "Are you sure? [y/N]: " && read ans && [ $${ans:-N} = y ]


# ===== CMD: Importer =====
.PHONY: build-importer
build-importer:
	@mkdir -p ${exec_build_dir}
	go build -o ${exec_build_dir}/importer/app ${exec_dir}/importer

.PHONY: run-importer
run-importer:
	REPO_ROOT=../../ ${exec_build_dir}/importer/app

.PHONY: dev-importer
dev-importer: build-importer
	REPO_ROOT=../../ ${exec_build_dir}/importer/app


# ===== CMD: Server =====
.PHONY: build-server
build-server:
	@mkdir -p ${server_build_dir}
	go build -o ${server_build_dir}/app ${server_dir}

.PHONY: run-server
run-server:
	${server_build_dir}/app

.PHONY: dev-server
dev-server: build-server
	REPO_ROOT=../../ ${server_build_dir}/app


# ===== SQL Goose =====
.PHONY: up
up:
	@set -a; . ${env_file}; set +a; \
	goose -dir ${sql_migrations_dir} ${sql_engine} "$$DB_URL" up

.PHONY: down
down:
	@set -a; . ${env_file}; set +a; \
	goose -dir ${sql_migrations_dir} ${sql_engine} "$$DB_URL" down
