.PHONY: bootstrap test lint intel-demo crypto-demo demos dashboard dashboard-bg dashboard-stop dashboard-build clean

PYTHON ?= .venv/bin/python
PIP ?= .venv/bin/pip

bootstrap:
	./scripts/bootstrap.sh

test:
	$(PYTHON) -m pytest -q

lint:
	$(PYTHON) -m ruff check .
	git diff --check

intel-demo:
	$(PYTHON) scripts/run_intel_demo.py

crypto-demo:
	$(PYTHON) scripts/run_crypto_demo.py

demos: intel-demo crypto-demo

dashboard:
	cd surface/dashboard && npm run dev -- --hostname 127.0.0.1 --port 3000

dashboard-bg:
	./scripts/start_dashboard.sh

dashboard-stop:
	./scripts/stop_dashboard.sh

dashboard-build:
	cd surface/dashboard && npm run build

clean:
	rm -rf .pytest_cache .ruff_cache **/__pycache__ surface/dashboard/.next
