dev-setup:
	@python3 -m venv venv
	@sh -c '. venv/bin/activate ; echo Installing requirements in venv created at $$VIRTUAL_ENV ; pip install -r requirements.txt'
	@echo "venv created; to activate use '. venv/bin/activate'"
