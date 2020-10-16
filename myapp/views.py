from django.shortcuts import render
import csv, io
from .models import Person, Person_detail
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from .forms import PersonForm, Person_detailForm

'''def person(request):
    template = "person_upload.html"

    if request.method =="POST":
        form = PersonForm(request.POST)

        if form.is_valid():
            form.save()
    else:
        form = PersonForm()
    context = {
        'form': form,
    }
    return render(request,template,context)

def person_detail(request):
    template = "person_upload.html"

    if request.method =="POST":
        form = Person_detailForm(request.POST)

        if form.is_valid():
            form.save()
    else:
        form = Person_detailForm()
    context = {
        'form': form,
    }
    return render(request,template,context)'''

@permission_required(('admin.can_add_log_entry'))
def person_upload(request):
    template = "person_upload.html"

    prompt = {
        'order': 'Order of CSV should be name, email, location'

    }
    if request.method =="GET":
        return render(request, template,prompt)
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for row in csv.reader(io_string,delimiter=',',quotechar="|"):
        _, created = Person.objects.update_or_create(
            name=row[1],
            email=row[2],
            location=row[3]
        )
    context = {}
    return render(request,template,context)


@permission_required(('admin.can_add_log_entry'))
def person_detail_upload(request):
    template = "person_upload.html"

    prompt = {
        'order': 'Order of CSV should be address, birth_date, phone'

    }
    if request.method =="GET":
        return render(request, template,prompt)
    csv_files = request.FILES['file']
    if not csv_files.name.endswith('.csv'):
        messages.error(request, 'This is not csv file')

    data_sets = csv_files.read().decode('UTF-8')
    io_string = io.StringIO(data_sets)
    next(io_string)

    for row in csv.reader(io_string,delimiter=',',quotechar='"'):
        print("address=" + row[2])
        email = row[1]
        user_id = Person.objects.values('id').filter(email=email)[0]['id']
        print( Person.objects.values('id').filter(email=email)[0]['id'])
        #print("after user_id")
        _, created = Person_detail.objects.update_or_create(
            person_id= Person.objects.get(id=user_id),
            address=row[2],
            birth_date=row[3],
            phone=row[4]

        )
    context = {}
    return render(request,template,context)



# Create your views here.
