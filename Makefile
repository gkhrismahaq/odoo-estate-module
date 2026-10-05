WEB_DB_NAME = odoo_17_module_dev
DB_USER = odoo
DB_PASSWORD = odoo
DOCKER = docker
DOCKER_COMPOSE = ${DOCKER} compose
CONTAINER_ODOO = odoo
CONTAINER_DB = odoo-postgres
help:
	@echo "Available commands:"
	@echo "  up			- Start the containers"
	@echo "  down			- Stop the containers"
	@echo "  restart		- Restart the containers"
	@echo "  console		- Open an Odoo shell in the Odoo container"
	@echo "  psql			- Open a PostgreSQL shell in the database container"
	@echo "  logs odoo		- Show logs for the Odoo container"
	@echo "  logs db		- Show logs for the database container"
	@echo "  addon <addon_name>	- Restart instance and update the specified addon"

start:
	$(DOCKER_COMPOSE) up -d
stop:
	$(DOCKER_COMPOSE) down
restart:
	$(DOCKER_COMPOSE) restart
console:
	$(DOCKER) exec -it $(CONTAINER_ODOO) odoo shell --db_host=$(CONTAINER_DB) -d $(WEB_DB_NAME) -r $(DB_USER) -w $(DB_PASSWORD)
psql:
	$(DOCKER) exec -it $(CONTAINER_DB) psql -U $(DB_USER) -d $(WEB_DB_NAME)

define log_target
	@if [ "$(1)" = "odoo" ]; then \
		$(DOCKER) logs -f $(CONTAINER_ODOO); \
	elif [ "$(1)" = "db" ]; then \
		$(DOCKER) logs -f $(CONTAINER_DB); \
	else \
		echo "Invalid argument. Use 'odoo' or 'db'."; \
	fi
endef

logs:
	$(call log_target,$(word 2,$(MAKECMDGOALS)))

define upgrade_addon
	$(DOCKER) exec -it $(CONTAINER_ODOO) odoo --db_host=$(CONTAINER_DB) -d $(WEB_DB_NAME) -r $(DB_USER) -w $(DB_PASSWORD) -u $(1) --stop-after-init
endef

addon: restart
	$(call upgrade_addon,$(word 2,$(MAKECMDGOALS)))

.PHONY: help start stop restart console psql logs odoo logs db