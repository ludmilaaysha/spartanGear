from django.contrib import admin
from spartangear.models import Categoria, Cor, Esporte, Foto, Produto, Tamanho
from users.models import PerfilUsuario

class FotoInline(admin.TabularInline):  # Pode ser StackedInline se preferir
    model = Foto
    extra = 1  # Quantidade de campos extras para foto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    inlines = [FotoInline]
    list_display = ('nome', 'preco', 'quantidade_estoque', 'destaque')

admin.site.register(PerfilUsuario)
admin.site.register(Categoria)
admin.site.register(Cor)
admin.site.register(Tamanho)
admin.site.register(Esporte)
admin.site.register(Foto)