# Facial-Recognition

### Requirements
1. Python 2.7 (https://www.python.org/download/releases/2.7.2/)
2. Python pip
3. OpenCV v2 (http://opencv.org/downloads.html)
4. A working webcam

### Installation
```
pip install -r requirements.txt
python setup.py install
```
or for development
```
pip install -r requirements.txt
python setup.py develop
```


### Yale Image Database
* Drop the 'yalefaces' folder in the root directory 
* http://vision.ucsd.edu/datasets/yale_face_dataset_original/yalefaces.zip


### Face detection instructions (face_recognizer.py)

Run like this:
```python
facerec recognize <selfie-folder>
```

To exit, press Ctrl+C
