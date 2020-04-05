# lazy-worksheets

This library is designed for language teachers to produce small worksheets for students using text/articles from websites.


## Installation instuctions
To import all the python dependencies in the terminal run:
`pip install -r requirements.txt`

In order to import the (English) language model go to the terminal and run:
`python -m spacy download en_core_web_sm `

To sort out the (potential) issues with nltk
see here:
https://stackoverflow.com/questions/54876404/unable-to-import-sqlite3-using-anaconda-python

Basically you need to find the sqlite3.dll which on ly computer was
in C:\Users\USER\anaconda3\Library\bin 
and paste it somewhere your virtual environment can find 
I put put here:
C:\Users\USER\.conda\envs\language-education\Scripts