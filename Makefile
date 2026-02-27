.PHONY: install lint test data demo clean help

help:
	@echo "TaelCore — available commands:"
	@echo "  make install    Install all dependencies"
	@echo "  make lint       Lint the library source"
	@echo "  make test       Run unit tests"
	@echo "  make data       Run data preparation notebook"
	@echo "  make demo       Run the main analysis notebook"
	@echo "  make clean      Remove cache files"

install:
	pip install -r requirements.txt

lint:
	flake8 Taelcore/ --max-line-length=127 --count --statistics

test:
	pytest Taelcore/tests/ -v --tb=short

data:
	jupyter nbconvert --to notebook --execute Data_preparation.ipynb \
		--output Data_preparation_executed.ipynb

demo:
	jupyter nbconvert --to notebook --execute Pain_Dimension_Reduction.ipynb \
		--output Pain_Dimension_Reduction_executed.ipynb

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -name "*.pyc" -delete
	find . -name ".DS_Store" -delete
	find . -name "*_executed.ipynb" -delete
