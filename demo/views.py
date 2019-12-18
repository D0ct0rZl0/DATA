from django.http import HttpResponse
from django.shortcuts import render
from .forms import FileUploadForm, SelectedHeadersForm
from .utils import classify_data_by_headers
import pandas as pd
import io


# Create your views here.


def index(request):
    if request.method == 'GET':
        form = FileUploadForm()
        return render(request, 'index.html', {'form': form})


def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            data_frame = pd.read_csv(io.StringIO(request.FILES['file'].read().decode('UTF-8')))
            request.session['data'] = data_frame.to_json(orient='records', force_ascii=False)
            return render(request, "index.html", {
                'headers': SelectedHeadersForm(),
                'form': FileUploadForm(),
                'data': data_frame
            })
    else:
        return render(request, 'index.html', {'headers': SelectedHeadersForm(), 'form': FileUploadForm()})


def calculate(request):
    headers = request.POST['json']
    data = request.session['data']
    fig = classify_data_by_headers(headers, data)
    return render(request, 'plot.html', {'figure': [fig]})
