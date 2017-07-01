from django.db import models
import datetime
# Create your models here.
# 이름 나이 생년월일 주소 핸드폰번호 사고위치 증상 사고원인 구조내용 구조사진
class Rescue(models.Model):
    name = models.CharField( verbose_name='이름', max_length=6 )
    age = models.IntegerField(verbose_name='나이',null=True)
    burth = models.DateField(verbose_name='생년월일',null=True)
    address = models.CharField(verbose_name='주소', max_length=40, blank=True, null=True,)
    phone = models.CharField( verbose_name='연락처', max_length=11,blank=True, null=True,
                              help_text="'-'없이 입력하세요 ex) 01012341234")
    date = models.DateField(verbose_name='날짜',auto_now_add=True)

    # 사고위치
    location = models.CharField(verbose_name='사고위치', max_length=10,null=True)
    symptom = models.CharField(verbose_name='증상', max_length=20,null=True)
    cause = models.CharField(verbose_name='원인', max_length=30,null=True)
    content = models.TextField(verbose_name='구조 내용',null=True)


class Attachment(models.Model):
    rescue = models.ForeignKey(Rescue, verbose_name='구조')
    file = models.FileField('첨부파일', upload_to='img')
