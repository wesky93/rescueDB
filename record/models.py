from django.db import models

# Create your models here.
# 이름 나이 생년월일 주소 핸드폰번호 사고위치 증상 사고원인 구조내용 구조사진
class RescueInfo(models.Model):
    """
    블로그 포스트 모델
    """
    name = models.ForeignKey('Category', blank=True, null=True, verbose_name='카테고리')
    age = models.CharField(verbose_name='제목', max_length=60)
    burth = models.DateTimeField(verbose_name='생일')
    address = models.CharField(verbose_name='요약', max_length=160, blank=True, null=True,
                                   help_text="포스트를 sns에 공유하거나 검색에서 노출될 포스트에 대한 요약입니다.")
    phone = ''

    # 사고위치
    location = models.CharField(verbose_name='사고위치', max_length=60)
    symptom = ""
    cause = ''
    content = models.TextField(verbose_name='구조 내용')
    picture = ''

    objects = models.Manager()

