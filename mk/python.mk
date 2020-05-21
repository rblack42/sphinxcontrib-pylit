.PHONY: run
run:    ## Run project application
	python3 -m $(PROJECT)

.PHONY: pyinit
pyinit:	## Create Python virtual environment
	test -d _venv || \
	python3 -m venv _venv && \
	source _venv/bin/activate && \
	pip install --upgrade pip

.PHONY: pyreqs
pyreqs: requirements.txt 	## Load Python requirements
	source _venv/bin/activate && \
	pip install -r requirements.txt

.PHONY: test
test: ## Run unit tests
	tox -v

.PHONY: changes
changes:	## create CHANGES file from git logs
	git log --oneline --pretty=format:"* %ad: %s\n" --date=short > CHANGES
