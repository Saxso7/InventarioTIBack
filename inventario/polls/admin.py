from django.contrib import admin

# Register your models here.
from .models import Notebook
from .models import Ram
from .models import Microfono
from .models import Mouse
from .models import Alcohol
from .models import AireComprimido
from .models import Refrigeracion
from .models import PlacaBase
from .models import Teclado
from .models import Adaptador
from .models import DiscosExternos

admin.site.register(Notebook)
admin.site.register(Ram)
admin.site.register(Microfono)
admin.site.register(Mouse)
admin.site.register(Alcohol)
admin.site.register(AireComprimido)
admin.site.register(Refrigeracion)
admin.site.register(PlacaBase)
admin.site.register(Teclado)
admin.site.register(Adaptador)
admin.site.register(DiscosExternos)
