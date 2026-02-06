from django import forms
from .models import Professor, Publicacao

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['nome', 'email', 'lattes', 'grande_area', 'area']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            # 'form-control' faz ocupar a largura toda
            # 'form-control-lg' aumenta a altura e a fonte do campo
            field.widget.attrs.update({'class': 'form-control form-control-lg', 'placeholder': field.label})

class PublicacaoForm(forms.ModelForm):
    class Meta:
        model = Publicacao
        fields = ['professor', 'titulo', 'ano', 'link']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'titulo':
                # Para o título, usamos Textarea para ser uma caixa grande
                field.widget = forms.Textarea(attrs={'rows': 3, 'class': 'form-control form-control-lg'})
            else:
                field.widget.attrs.update({'class': 'form-control form-control-lg'})
