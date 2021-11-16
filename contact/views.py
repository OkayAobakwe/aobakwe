from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.
def contact_me(request):
	if request.method != 'POST':
		form = ContactForm()
	else:
		form = ContactForm(data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('blog:index')

	context = { 'form': form}
	return render(request, 'contact/contact_me.html', context)