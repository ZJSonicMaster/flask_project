from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired


class SearchForms(Form):
    # 至少有一个字符，长度限制
    #DataRequired 防止传入空值
    q = StringField(DataRequired(),validators = [Length(min = 1, max = 30, message = '参数q不符合规范')])

    # 正整数，最大值限制
    page = IntegerField(validators = [NumberRange(min = 1, max = 99)], default = 1)