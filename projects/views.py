from django.shortcuts import render


# Create your views here.
def project_index(request):
	context = {'my_url': "https://sand-logs.herokuapp.com/"}
	return render(request, 'projects/project_index.html', context)

