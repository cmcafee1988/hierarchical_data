from django.shortcuts import render, HttpResponseRedirect, reverse
from file_system.models import Show_Files
from file_system.forms import AddFilesForm
# Create your views here.


def show_files(request):
    return render(request, 'files.html', {'files': Show_Files.objects.all()})


def add_files(request):
    html = 'genericform.html'

    if request.method == 'POST':
        form = AddFilesForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Show_Files.objects.create(
                name=data['name'],
                parent=data['parent']
            )
        return HttpResponseRedirect(reverse('homepage'))

    form = AddFilesForm()
    return render(request, html, {'form': form})
# Create your views here.
