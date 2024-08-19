PYTHON_FILES := $(shell find src -name "*.py" -not -name "__init__.py")

.PHONY: help
help:     ## Show the help.
	@echo "Usage: make <target>"
	@echo ""
	@echo "Targets:"
	@fgrep "##" Makefile | fgrep -v fgrep

.PHONY: clean
clean:    ## Cleans custom files and directories.
	@rm -rf reports/ || true
	@rm -f .coverage || true

.PHONY: lint
lint:     ## Lints the Python code.
	@echo "==============="
	@echo "Linting code..."
	@echo "==============="
	@mkdir -p reports/lint-reports || true
	@pipenv run pylint $(PYTHON_FILES) 2>&1 | tee reports/lint-reports/pylint-report.txt || true
	@echo "Lint report generated at reports/lint-reports/pylint-report.txt"

.PHONY: fmt
fmt:      ## Formats the Python code.
	@echo "=================="
	@echo "Formatting code..."
	@echo "=================="
	@pipenv run black $(PYTHON_FILES)

.pHONY: test
test:     ## Test the Python code (configuration based on the 'pytest.ini' file).
	@echo "=================="
	@echo "Executing tests..."
	@echo "=================="
	@mkdir -p reports/tests-reports || true
	@pipenv run pytest 2>&1 | tee reports/tests-reports/pytest-report.txt || true
	@echo "Test report generated at reports/tests-reports/pytest-report.txt"

.PHONY: run
run:      ## Executes the application locally.
	@echo "============================"
	@echo "Running Flask application..."
	@echo "============================"
	@pipenv run python -m flask --app src.app run --debug
