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