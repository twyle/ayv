build:
	@python setup.py sdist bdist_wheel

clean:
	@rm -rf build dist youtube.*

test-upload:
	@twine upload --repository testpypi dist/*

bump-tag:
	@cz bump --changelog