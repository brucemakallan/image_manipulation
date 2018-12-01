# image_manipulation
Resize, Rename, ...

#####Setup:
1. Create virtual env
`python3 -m venv env`

2. Start env
`source env/bin/activate`

3. Install requirements
`pip install -r requirements.txt`

4. Set directory for images in main.py:
e.g. `my_path = r'Users/test/myImages/'`
*NB: Add the trailing slash*

5. Set required `WIDTH_IN_PX`
*The height will be calculated automatically to maintain aspect ratio*

#####Run app:
`python -m main`
