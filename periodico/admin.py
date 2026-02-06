from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Professor, Publicacao



class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'grande_area', 'area') # Colunas na lista
    search_fields = ('nome',) # Barra de busca
    list_filter = ('grande_area', 'area')

class PublicacaoAdmin(admin.ModelAdmin):
    # Colunas que aparecerão na lista

    list_display = ('titulo', 'professor', 'ano', 'link_curto')
    
    # Filtros na lateral direita
    list_filter = ('professor', 'ano')
    
    # Barra de busca no topo (busca no título e no nome do professor relacionado)
    search_fields = ('titulo', 'professor__nome')
    # Organização do formulário de cadastro (Design Clean)
    autocomplete_fields = ['professor']

    fieldsets = (
        ('Informações Básicas', {
            'fields': ('titulo', 'professor')
        }),
        ('Detalhes da Publicação', {
            'fields': ('ano', 'link'),
            'description': 'Insira os dados técnicos e o link da fonte original.'
        }),
    )

    # Função para mostrar um link clicável na lista do admin
    def link_curto(self, obj):
        if obj.link:
            return "Sim"
        return "Não"
    link_curto.short_description = "Possui Link?"
    
admin.site.register(Professor,ProfessorAdmin)
admin.site.register(Publicacao,PublicacaoAdmin)
