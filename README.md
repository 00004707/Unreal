# Unreal Engine 5 Personal Docs

Personal documentation made using Sphinx

Uses [furo](https://github.com/pradyunsg/furo) theme

Using extensions
* [sphinx-copybutton](https://pypi.org/project/sphinx-copybutton/) 
* [sphinxext-opengraph](https://pypi.org/project/sphinxext-opengraph/)
* [sphinx_favicon](https://pypi.org/project/sphinx-favicon/)
* [sphinx-notfound-page](https://github.com/readthedocs/sphinx-notfound-page)
* [sphinx-hoverxref](https://github.com/readthedocs/sphinx-hoverxref)
* [sphinx-last-updated-by-git](https://github.com/mgeier/sphinx-last-updated-by-git)

and also

* [sphinx-autobuild](https://github.com/executablebooks/sphinx-autobuild) (optional)

## How to view the docs

uhhhhhh todo

## How to run this on your own

1. Get Python 3.11.4
1. Install extensions

        pip install sphinx furo sphinx-copybutton sphinxext-opengraph sphinx_favicon

1. Install autobuilder if you want automatic building on changes

        pip install sphinx-autobuild

1. Clone repo & go to root directory
1. Build using ```sphinx-build source build``` or use ```make.bat``` files if you're on Windows
1. If you installed the autobuilder run ```sphinx-autobuild source build/html``` to watch for changes in source files or use ```autobuild_start.bat``` files if you're on Windows
1. you won (yipeee)