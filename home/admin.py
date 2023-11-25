from django.contrib import admin

# Register your models here.
from home.models import BusinessToNext, Concept, NeedHelp, Plan, Design, Build, QualityAssurance,Delivery, About, Services, Clients,BlogPost,Blog

admin.site.register(BusinessToNext)
admin.site.register(Concept)
admin.site.register(Plan)
admin.site.register(Design)
admin.site.register(Build)
admin.site.register(QualityAssurance)
admin.site.register(Delivery)
admin.site.register(About)
admin.site.register(Services)
admin.site.register(NeedHelp)
admin.site.register(Clients)
admin.site.register(BlogPost)
admin.site.register(Blog)



