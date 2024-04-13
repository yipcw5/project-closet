# project-closet

Keep track of what's in the closet, in case something gets pushed to the back IRL and risks being forgotten for eternity.

## Installations / Setup

Python 3.10+ is required.

```
pip3 install -r requirements.txt
cd src
python3 main.py
```

Due to the nature of filepath referencing, do not attempt running `main.py` from the project root folder.

### To run unit tests:
```
export PYTHONPATH=/Documents/GitHub/project-closet:$PYTHONPATH
pytest --cov=. tests/ --cov-report xml:cov.xml # pytest --cov=. is not enough for Coverage Gutters to display code coverage.
```

Recommended extensions:
Coverage Gutters

### Local DB

PostgreSQL is used to store info on clothes. To run locally, ensure this has been installed on Homebrew (Mac), along with PGAdmin. (Credits to https://www.sqlshack.com/setting-up-a-postgresql-database-on-mac/)
```
brew install postgresql
brew services start postgresql

# Do whatever you need, then ensure you stop running the service:
brew services stop postgresql
```

## Workflow

Input: a pic of a new item of clothing, any format

Will convert to standard JPG/PNG
And add to image folder db
Based on categories added

## Ideas
- Use ML to recognise image inputs: https://www.udacity.com/course/intro-to-tensorflow-for-deep-learning--ud187
- Use gRPC calls to trigger daily alerts to enter OOTD entry
- Somehow make matching outfit suggestions
- Bags & shoes