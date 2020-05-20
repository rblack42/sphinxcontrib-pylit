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

.PHONY: text
test: ## Run unit tests with tox
	pip uninstall -y sphinxcontrib-lpblocks && \
	pip install . && \
	tox -v
