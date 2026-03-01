# Formatting
format:
	@pipenv run black src

format-check:
	@pipenv run black src --check


# Static typing
mypy-check:
	@pipenv run mypy src


# Import sorting
isort:
	@pipenv run isort src

isort-check:
	@pipenv run isort src --check-only

# Quality checks
quality-checks:
	@echo "$(CYAN)$(BOLD)-----------  Black checkings:  -----------$(NC)"
	@$(MAKE) format-check
	@echo "\n$(CYAN)$(BOLD)-----------  MyPy checkings:  -----------$(NC)"
	@$(MAKE) mypy-check
	@echo "\n$(CYAN)$(BOLD)-----------  Isort checkings:  -----------$(NC)"
	@$(MAKE) isort-check

##################### Helper constants
# Colors
CYAN = \033[0;36m
BOLD = \033[1m
NC = \033[0m# No Color
