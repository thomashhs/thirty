from django.http import HttpResponse,HttpResponseRedirect
import datetime
from django.shortcuts import render
from books.models import Book
from books.forms import ContactForm


def hello(request):
    html=[]
    for k,v in request.META.items():
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def current_time(request):
    now=datetime.datetime.now()
    return render(request,'time.html',{'now':now})

def search(request):
    error=False
    if 'q' in request.GET:
        q=request.GET['q']
        if not q:
            error=True
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request,'search_results.html',
                                  {'books': books, 'query': q})
    return render(request,'search_form.html', {'error': error})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render(request,'contact_form.html', {'form': form})

