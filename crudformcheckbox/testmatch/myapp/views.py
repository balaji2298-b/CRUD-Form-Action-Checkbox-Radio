from django.shortcuts import render,redirect
from myapp.models import Checkbox
from django.contrib import messages
from myapp.forms import CheckboxForm

def index(request):
	checkboxs = Checkbox.objects.all()
	context = {'checkboxs': checkboxs}
	return render(request,'index.html', context)

def create(request):
	if request.method == "POST":
		name = request.POST.get("name")
		language = request.POST.getlist("language")
		tmpallvals = ','.join(language)
		gender = request.POST.get("gender")
		checkbox = Checkbox(name=name,language=tmpallvals,gender=gender)
		checkbox.save()
		messages.info(request,'Successfully Registered')
		return redirect("/")
	return render(request,'index.html')

def update(request,id):
	checkboxs = Checkbox.objects.get(id=id)
	if request.method == "POST":
		form = CheckboxForm(request.POST,instance=checkboxs)
		if form.is_valid():
			form.save()
			messages.warning(request,'Successfully Updated')
			return redirect('index')
	else:
		form = CheckboxForm(instance=checkboxs)
	return render(request,'update.html',{'form':form})
	
def delete(request,id):
	checkboxs = Checkbox.objects.get(id=id)
	checkboxs.delete()
	messages.error(request,'Successfully Deleted')
	return redirect("/")