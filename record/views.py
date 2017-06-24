from django.shortcuts import render
from django.views.generic import ListView,DetailView,TemplateView,CreateView,FormView
from .forms import RescueForm
from .models import Rescue
# Create your views here.
class Home(TemplateView):
    """
    메인 버튼 노출 뷰
    """
    pass

class Input(CreateView):
    """
    구조 정보 입력
    """
    model = Rescue
    form_class = RescueForm
    template_name = 'record/form.html'
    success_url = '?success'


class Records(ListView):
    """
    구조기록 목록 뷰
    """

    pass

class Detail(DetailView):
    """
    구조 정보 상세 뷰뷰
   """
    pass

