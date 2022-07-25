from django.forms import ModelForm
from .models import Project

class ProjectForm(ModelForm):

    class Meta:
        model = Project
        fields = ["title", "thumbnail", "body"] #"__all__"

def __init__(self, *arg, **kwargs):
    super(ProjectForm, self).__init__(*args, **kwargs)
    self.fields['title'].widget.attrs.update(
        {
            'class': "form-control"
        }
    )

    self.fields['body'].widget.attrs.update(
        {
            'class': "form-control"
        }
    )