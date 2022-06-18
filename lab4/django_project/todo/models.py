from django.db import models


class Todo(models.Model):
    name = models.fields.CharField(verbose_name="Todo Name", max_length=100, unique=True)
    priority = models.fields.IntegerField(verbose_name="Todo Priority", default=1)
    todo_date = models.fields.DateField(verbose_name="Date", default='2000-01-01')
    is_done = models.fields.BooleanField(default=False)
    notes = models.fields.TextField(default='')

    creation_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Todo: {self.name} At Time {self.creation_time}"

    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'
        ordering = ('-creation_time',)


class Task(models.Model):
    name = models.fields.CharField(verbose_name="Task Name", max_length=100)
    todo = models.ForeignKey('todo', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Task {self.id} For Todo : {self.todo.name}"



