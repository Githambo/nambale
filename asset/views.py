from django.shortcuts import render,redirect
from django.views.generic import CreateView,DetailView,UpdateView,DeleteView,ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
# Create your views here.

from asset.forms import AdditionForm
from asset.models import Asset
import csv


def index(request):
	template_name='base.html'
	return render(request,template_name)

class AssetDetail(LoginRequiredMixin,DetailView):
	model=Asset
def siteconfig_view(request):
  """ Site Config View """
  if request.method == 'POST':
    form = SiteConfigForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, 'Configurations successfully updated')
      return HttpResponseRedirect('site-config')
  else:
    form = SiteConfigForm(queryset=SiteConfig.objects.all())

  context = {"formset": form, "title": "Configuration"}
  return render(request, 'asset/siteconfig.html', context)

class MassAddition(LoginRequiredMixin, SuccessMessageMixin, CreateView):
  form_class = AdditionForm
  template_name = 'asset/mgt_form.html'
  success_url = reverse_lazy('asset:addition')
  success_message = 'New Asset successfully added'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['title'] = 'Add New Asset'
      return context


@login_required
def SearchView(request):
	template_name='asset/asset_search.html'
	if request.method =='GET':
		query=request.GET.get('q')
		submitbutton=request.GET.get('submit')

		if query is not None:
			results=Asset.objects.filter(Q(tag_number__icontains=query)|Q(asset_description__icontains=query))
			return render(request,template_name,{'results':results,'submitbutton':submitbutton}) 		 	
		else:
			return render(request,template_name)
	else:
		return render(request,template_name)



@login_required
def register_download(request):
	response=HttpResponse(content_type='text/csv')
	response['Content-Disposition']='attachment;filename="asset_register.csv"'
	query=Asset.objects.all()

	writer=csv.writer(response)
	writer.writerow(['DESCRIPTION','CATEGORY','TAG NUMBER','SERIAL NUMBER','LOCATION','DATE_IN_SERVICE'])
	
	for rows in query:
		writer.writerow([rows.asset_description,rows.category,rows.tag_number,rows.serial_number,rows.location,rows.date_in_service])
	

	return response
