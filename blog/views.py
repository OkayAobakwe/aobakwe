from django.shortcuts import render, get_object_or_404
from .models import Entry
from .forms import CommentForm

# Create your views here.
def index(request):
	context = {
		'twitter_url': "https://twitter.com/oh_aobakwe", 
		'instagram_url': "https://instagram.com/aobakweokay",
		'github_url': "https://github.com/OkayAobakwe",
	}
	return render(request, 'blog/index.html', context)

def blog(request):
	entries = Entry.objects.order_by('date_added')
	context = {
		'entries': entries
	}
	return render(request, 'blog/blog.html', context)

def entry(request, entry_id):
	entry = Entry.objects.get(id=entry_id)
	comments = entry.comments.filter(active=True)
	new_comment = None

	if request.method != "POST":
		comment_form = CommentForm()
	else:
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():
			new_comment = comment_form.save(commit=False)
			new_comment.entry = entry
			new_comment.save()

	context ={'entry': entry, 'comments': comments, 'new_comment': new_comment,
				'comment_form': comment_form,}
	return render(request, 'blog/entry.html', context)