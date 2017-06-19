from django.shortcuts import render
from django.views.generic import ListView,DetailView,TemplateView,CreateView
from .models import RescueInfo
# Create your views here.
class Home(TemplateView):
    """
    메인 버튼 노출 뷰
    """
    pass

class Input(CreateView):
    model = RescueInfo
    """
    구조 기록 입력 뷰
    """
    pass

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

