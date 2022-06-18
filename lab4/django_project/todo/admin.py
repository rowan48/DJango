from django.contrib import admin
from .models import Todo, Task


class TaskInline(admin.StackedInline):
    model = Task
    extra = 1


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['name', 'priority', 'is_done', 'creation_time', 'update_time', 'my_custom_function_field']
    search_fields = ['name', 'notes']
    list_filter = ('priority',)
    fieldsets = (
        ('Main Section', {'fields': ['name', 'priority', 'is_done', 'my_custom_function_field']}),
        ('Dates Section', {'fields': ['creation_time', 'update_time']}),
        ('Notes', {'fields': ['notes']}),
    )

    inlines = [TaskInline]

    readonly_fields = ['creation_time', 'update_time', 'is_done', 'my_custom_function_field']

    def my_custom_function_field(self, obj):
        task_names = ','.join([task_obj.name for task_obj in obj.task_set.all()])

        return f"Tasks Names: {task_names}"
        # return f"{obj.name} Priority: {obj.priority}"

    my_custom_function_field.short_description = 'My FUnction'

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_add_permission(self, request):
        return True


class TaskAdmin(admin.ModelAdmin):
    list_filter = ('todo__is_done', 'todo__priority')


admin.site.register(Task, TaskAdmin)
