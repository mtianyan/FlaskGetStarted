# encoding: utf-8
__author__ = 'mtianyan'
__date__ = '2018/2/12 0012 00:34'
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, FileField, TextAreaField,IntegerField
from wtforms.validators import DataRequired, EqualTo, ValidationError
from models import User
from flask import session as form_session

"""
登录表单:
1. 账号
2. 密码
3. 登录按钮
"""


class LoginForm(FlaskForm):
    account = StringField(
        validators=[
            DataRequired(u"账号不能为空")
        ],
        description=u"账号",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入账号"
        }
    )
    pwd = PasswordField(
        validators=[
            DataRequired(u"密码不能为空")
        ],
        description=u"密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入密码"
        }
    )
    submit = SubmitField(
        u"登录",
        render_kw={
            "class": "btn btn-primary"
        }
    )

    def validate_pwd(self, field):
        pwd = field.data
        user = User.query.filter_by(account=self.account.data).first()
        if not user.check_pwd(pwd):
            raise ValidationError(u"密码不正确")


"""
注册表单:
1. 账号
2. 密码
3. 确认密码
4. 验证码
5. 注册按钮
"""


class RegisterForm(FlaskForm):
    account = StringField(
        validators=[
            DataRequired(u"账号不能为空")
        ],
        description=u"账号",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入账号"
        }
    )
    pwd = PasswordField(
        validators=[
            DataRequired(u"密码不能为空")
        ],
        description=u"密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入密码"
        }
    )
    re_pwd = PasswordField(
        validators=[
            DataRequired(u"确认密码不能为空"),
            EqualTo('pwd', message="两次密码不一致！")
        ],
        description=u"确认密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请确认密码"
        }
    )
    captcha = StringField(
        validators=[
            DataRequired(u"验证码不能为空"),
        ],
        description=u"验证码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入验证码"
        }
    )
    submit = SubmitField(
        u"注册",
        render_kw={
            "class": "btn btn-primary"
        }
    )

    # 自定义字段验证规则: validate 下划线 字段名
    def validate_account(self, field):
        account = field.data
        user = User.query.filter_by(account=account).count()
        if user > 0:
            raise ValidationError(u"账号已存在")

     # 自定义验证码规则: validate 下划线 字段名
    def validate_captcha(self, field):
        captcha = field.data
        if not form_session["captcha"]:
            raise ValidationError(u"非法操作")
        if form_session["captcha"].lower() != captcha.lower():
            raise ValidationError(u"验证码不正确")


"""
发布文章表单:
1. 标题
2. 分类
3. 封面
4. 内容
5. 发布文章按钮
"""


class ArticleAddForm(FlaskForm):
    title = StringField(
        validators=[
            DataRequired(u"标题不能为空")
        ],
        description=u"标题",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入标题"
        }
    )
    # 强制类型为整型
    category = SelectField(
        validators=[
            DataRequired(u"分类不能为空")
        ],
        description=u"分类",
        choices=[(1, u"科技"), (2, u"搞笑"), (3, u"军事")],
        default=3,
        coerce=int,
        render_kw={
            "class": "form-control"
        }
    )
    logo = FileField(
        validators=[
            DataRequired(u"请上传封面")
        ],
        description=u"封面",
        render_kw={
            "class": "form-control-file",
            "style": "margin-left: 2px;"
        }
    )
    content = TextAreaField(
        validators=[
            DataRequired(u"内容不能为空")
        ],
        description=u"内容",
        render_kw={
            "style": "height:300px;",
            "id": "content"
        }
    )
    submit = SubmitField(
        u"发布文章",
        render_kw={
            "class": "btn btn-primary"
        }
    )


class ArticleEditForm(FlaskForm):
    id = IntegerField(
        validators=[
            DataRequired(u"编号不能为空")
        ],
    )
    title = StringField(
        validators=[
            DataRequired(u"标题不能为空")
        ],
        description=u"标题",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入标题"
        }
    )
    # 强制类型为整型
    category = SelectField(
        validators=[
            DataRequired(u"分类不能为空")
        ],
        description=u"分类",
        choices=[(1, u"科技"), (2, u"搞笑"), (3, u"军事")],
        default=3,
        coerce=int,
        render_kw={
            "class": "form-control"
        }
    )
    logo = FileField(
        validators=[
            DataRequired(u"请上传封面")
        ],
        description=u"封面",
        render_kw={
            "class": "form-control-file",
            "style": "margin-left: 2px;"
        }
    )
    content = TextAreaField(
        validators=[
            DataRequired(u"内容不能为空")
        ],
        description=u"内容",
        render_kw={
            "style": "height:300px;",
            "id": "content"
        }
    )
    submit = SubmitField(
        u"编辑文章",
        render_kw={
            "class": "btn btn-primary"
        }
    )