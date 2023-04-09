from django import forms

from users.models import FileModel


class FileForm(forms.Form):
    # title = forms.CharField(max_length=50)
    file = forms.FileField(
        # 支持多文件上传
        widget=forms.ClearableFileInput(attrs={
            'multiple': True,
            # 'class': 'btn app-btn-primary'
        }),

        # label='请选择文件',
    )
    class Meta:
        model = FileModel
        fields = ('file')
    def __init__(self, *args, **kwargs):
        super(FileForm, self).__init__(*args, **kwargs)
        self.fields['file'].widget.attrs.update({'class': 'btn app-btn-primary'})
