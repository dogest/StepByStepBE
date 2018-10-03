from django.contrib import admin

from Plan.models import Plan, PlanProblem, PlanUser

admin.site.register(Plan)
admin.site.register(PlanProblem)
admin.site.register(PlanUser)
