#!/usr/bin/env bash
cd rst && \
sphinx-build -b pseudoxml -d _build/doctrees . _build/xml
