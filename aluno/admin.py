from django.contrib import admin
from aluno.models import *

admin.site.register(Aluno)
admin.site.register(Disciplina)
admin.site.register(AlunoDisciplina)