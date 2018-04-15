from flask import Flask
from wtforms import Form, TextAreaField,FileField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired, InputRequired




class UploadForm(Form):
    photo = FileField('Photo',validators=[FileRequired('Upload a photo please'), FileAllowed(['jpg', 'png'], 'Images only!')
    ])
    description = TextAreaField('Description',validators=[InputRequired(message='Description Needed')])


