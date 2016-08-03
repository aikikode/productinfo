ENV := venv

.PHONY: venv
venv: $(ENV)/bin/activate

$(ENV)/bin/activate:
	test -d $(ENV) || virtualenv -p /usr/bin/python3.5 $(ENV) || virtualenv -p /usr/bin/python3 $(ENV)
	$(ENV)/bin/pip install -U pip
	$(ENV)/bin/pip install -U -r pip.requirements.txt
	touch $(ENV)/bin/activate

clean:
	rm -rf $(ENV)
