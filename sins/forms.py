from django.forms import Form, ModelForm
from captcha.fields import ReCaptchaField

from sins.models import Sinner, Sin


class VoteForCost(Form):
    pass


class CreateYourSinForm(ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Sin
        fields = ['text', 'cost', 'target_sex', 'language', 'captcha']


class AboutQuestionnaire(ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Sinner
        fields = ['age', 'sex', 'occupation', 'religion', 'country_of_residence', 'captcha']
