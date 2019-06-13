from flask import Flask, render_template, request

from wtforms import Form
from wtforms import fields, validators
from wtforms.ext.sqlalchemy.fields import QuerySelectField

app = Flask(__name__)

class SetDataParamsForm(Form):
    ticker = fields.StringField()
    year = fields.IntegerField('Year', [validators.NumberRange(min=2005, max=2019)])
    month = fields.IntegerField('Month', [validators.NumberRange(min=1, max=12)])

  #  site = QuerySelectField(query_factory=Site.query.all)

@app.route('/')
def index():
    set_data_params_form = SetDataParamsForm()
    return render_template('index.html', set_data_params_form=set_data_params_form)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(port=33507)
