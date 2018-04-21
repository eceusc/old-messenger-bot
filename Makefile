#!/bin/bash
.DEFAULT_GOAL := install
.PHONY: clean init install run

clean: ; ( \
	rm -rf venv; \
	)

init: ; ( \
	make clean; \
	virtualenv venv; \
  )
install: ; ( \
	python3 -m venv venv/bin/activate; \
	pip3 install -r requirements.txt; \
  )
run: ; ( \
	python3 manage.py runserver 8000;  \
	)
ngrok: ; ( \
	~/ngrok http 8000; \
	)
