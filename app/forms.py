from flask_wtf import FlaskForm
from wtforms import TextAreaField,FileField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired, InputRequired




class UploadForm(FlaskForm):
    description = TextAreaField('Description',validators=[InputRequired(message='Description Needed')])
    photo = FileField('Photo',validators=[FileRequired('Upload a photo please'), FileAllowed(['jpg', 'png'], 'Images only!')])
