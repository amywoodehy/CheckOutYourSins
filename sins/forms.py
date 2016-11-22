from django.forms import Form, ModelForm
from captcha.fields import ReCaptchaField

from sins.models import Sinner, Sin


class VoteForCost(Form):
    pass


class CreateYourSinForm(ModelForm):
    model = Sin
    captcha = ReCaptchaField()


class AboutQuestionnaire(ModelForm):
    model = Sinner
    captcha = ReCaptchaField()
