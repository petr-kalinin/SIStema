from django import forms

import frontend.forms
import modules.ejudge.models


class EntranceTaskForm(forms.Form):
    def __init__(self, task, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['solution'].widget.attrs['id'] = '%s_%d' % (self.task_type, task.id)


class TestEntranceTaskForm(EntranceTaskForm):
    task_type = 'test'

    solution = forms.CharField(max_length=100,
                               label='Ответ',
                               label_suffix='',
                               widget=forms.TextInput(),
                               )


class FileEntranceTaskForm(EntranceTaskForm):
    task_type = 'file'

    solution = frontend.forms.RestrictedFileField(max_upload_size=5 * 1024 * 1024,
                                                  required=True,
                                                  label='Выберите файл с решением',
                                                  label_suffix='')


class ProgramEntranceTaskForm(EntranceTaskForm):
    task_type = 'program'

    language = forms.ModelChoiceField(queryset=modules.ejudge.models.ProgrammingLanguage.objects.all(),
                                      to_field_name='id',
                                      required=True,
                                      empty_label='Язык программирования',
                                      label='Язык программирования',
                                      label_suffix='')

    solution = frontend.forms.RestrictedFileField(max_upload_size=512 * 1024,
                                                  required=True,
                                                  label='Выберите файл с программой',
                                                  label_suffix='')
