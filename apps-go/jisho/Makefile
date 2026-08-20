main_package_dir = ./cmd
build_dir = ./bin
env_file = ../../.env

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
	@mkdir -p ${build_dir}/importer
	go build -o ${build_dir}/importer/app ${main_package_dir}/importer

.PHONY: run-importer
run-importer:
	${build_dir}/importer/app

.PHONY: dev-importer
dev-importer: build-importer
	${build_dir}/importer/app


# ===== CMD: Server =====
.PHONY: build-server
build-server:
	@mkdir -p ${build_dir}/server
	go build -o ${build_dir}/server/app ${main_package_dir}/server

.PHONY: run-server
run-server:
	${build_dir}/server/app

.PHONY: dev-server
dev-server: build-server
	${build_dir}/server/app


# ===== SQL Goose =====
.PHONY: up
up:
	@set -a; . ${env_file}; set +a; \
	goose -dir ${sql_migrations_dir} ${sql_engine} "$$DB_URL" up

.PHONY: down
down:
	@set -a; . ${env_file}; set +a; \
	goose -dir ${sql_migrations_dir} ${sql_engine} "$$DB_URL" down
