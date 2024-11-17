from django.shortcuts import render, get_object_or_404, redirect

from .models import Record
from django.http import HttpResponseRedirect
from django.views import generic
from . import forms


def delete(request, email, cname, dc):
    rec = get_object_or_404(Record, pk = (email, cname, dc))
    rec.delete()
    return redirect('create')
def update(request, email, cname, dc):
    obj = get_object_or_404(Record, pk = (email, cname, dc))
    form = forms.Update(instance=obj)
    if request.method == "POST":
        form = forms.Update(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('create')

    template_name = "update.html"
    context = {"form": form}
    return render(request, template_name, context)

def create(request):
    if request.method == "POST":
        form = forms.Create(request.POST)
        if form.is_valid():
            newrec = form.save(commit = True)
            newrec.save()
            return redirect("create")
    else:
        form = forms.Create()
    recs = Record.objects.order_by('total_patients')
    template_name = "display_reports.html"
    context = {"form": form , "recs" : recs}
    return render(request, template_name, context)
