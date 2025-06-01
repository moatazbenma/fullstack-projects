from tasks.forms import TaskForm



def test_valid_form(self):
    data = {'title': 'New Task'}
    form = TaskForm(data=data)
    self.assertTrue(form.is_valid())