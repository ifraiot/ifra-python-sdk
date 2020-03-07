
upload:
	python -m twine upload dist/*

build:
	python setup.py bdist_wheel

clear:
   rm -rf build

