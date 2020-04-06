# How to build a dash app

## Step 1 - Create a virtual environment for dash
* in your terminal run `conda create -n 'dash-env' python=3.6`
* or just copy your `learn-env` to a `dash-env` using:
	* conda create --clone learn-env --name dash-env
* after that, verify your installation with `conda env list`
* install all of your dependencies for this environment


## Step 2 - Create your project folder
Your project folder should have this structure
```
project-folder/
|-app.py
|__init__.py
|-components/
	|-files.py
	|-__init__.py
|-data/
	|-datafiles
|assets/
    |-cssfiles.css
    |-imagefiles.png
```

* Step 3 - Populate your app.py file

# Study Group Itinerary
* Setup up working Environment in Pycharm
* Create a base app and run it
* Add a second line H2 that says "Hello {Your name}!"
* Add an input box to take in a string
* Add callbacks to modify the H2 Header
* Add iris dataset graph

# Enjoy!
