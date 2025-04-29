from django.contrib import admin
from .models import Department
from .models import User
from .models import Team
from .models import Health_Check_Card
from.models import Senior_Lead
from.models import Department_Leaders

admin.site.register(Department)
admin.site.register(User)
admin.site.register(Team)
admin.site.register(Health_Check_Card)
admin.site.register(Senior_Lead)
admin.site.register(Department_Leaders)

# Register your models here.
