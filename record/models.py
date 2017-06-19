from django.db import models

# Create your models here.
# 이름 나이 생년월일 주소 핸드폰번호 사고위치 증상 사고원인 구조내용 구조사진
class RescueInfo(models.Model):
    name = models.CharField( verbose_name='이름', max_length=6 )
    age = models.IntegerField(verbose_name='나이')
    burth = models.DateTimeField(verbose_name='생년월일')
    address = models.CharField(verbose_name='요약', max_length=40, blank=True, null=True,)
    phone = models.CharField( verbose_name='연락처', max_length=11,blank=True, null=True,
                              help_text="'-'없이 입력하세요 ex) 01012341234")

    # 사고위치
    location = models.CharField(verbose_name='사고위치', max_length=10)
    symptom = models.CharField(verbose_name='증상', max_length=20)
    cause = models.CharField(verbose_name='원인', max_length=30)
    content = models.TextField(verbose_name='구조 내용')
    picture = models.ImageField()

    objects = models.Manager()

