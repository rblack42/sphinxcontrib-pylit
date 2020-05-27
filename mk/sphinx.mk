.PHONY:	docs
docs:	changes	## run Sphinx to build html pages
	pip install -e . && \
	cd rst && \
	sphinx-build -b html -d _build/doctrees . ../docs

.PHONY:	docs-clean
docs-clean:
		rm -rf rst/_build/doctrees

.PHONY: latex
latex:
	pip install . && \
	cd rst && \
	sphinx-build -b latex -d _build/doctrees . _build/latex

