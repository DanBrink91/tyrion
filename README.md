tyrion
======

## How To Install

```
mkvirtualenv tyrion (optional)
pip install -r requirements
```

Django will install from trunk. To get the latest updates do a "git pull" inside the django directory.

## Adding Python Dependencies

All Python based dependencies should be installed using pip. Before pushing run the following command in the root directory.

```
pip freeze | sed 's/@[a-z0-9]\+//' > requirements.txt
```

Note: If you're not running in a virtualenv be sure to cleanup the requirements file to contain only the neccessary requirements.