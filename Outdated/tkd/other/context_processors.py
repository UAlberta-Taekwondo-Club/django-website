from main.models import Form

def add_variable_to_context(request):
	if (Form.objects.order_by('-date_posted').first()):
		return {'newest_form_id': Form.objects.order_by('-date_posted').first().id}
	else:
		return {'newest_form_id': 0}