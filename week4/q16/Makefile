.PHONY: check build clean

check:
	bash check.sh

build:
	py -m build

clean:
	rm -rf dist build src/*.egg-info
	find . -name __pycache__ -type d -exec rm -rf {} + 2>/dev/null || true
	find . -name "*.pyc" -delete 2>/dev/null || true

