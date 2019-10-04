from django.db import models

# Weight 파일을 저장하는 db 테이블 형태, title 200자 제한, 저장 경로 설정, 생성 및 수정일 자동 추가
class WeightFile(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, default='no title')
    weight_file = models.FileField(blank = False, upload_to="WeightFile/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 각 데이터를 출력할 때 id 값 + title 조합으로 표시
    def __str__(self):
        return str(self.id) +' : ' + self.title

    # def summary(self):
    #     return self.body[:100]

# Image 파일을 저장하는 db 테이블 형태, title 200자 제한, 저장 경로 설정, 생성 및 수정일 자동 추가
class ImageFile(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, default='no title')
    image_file = models.FileField(blank = False, upload_to="ImageFile/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 각 데이터를 출력할 때 id 값 + title 조합으로 표시
    def __str__(self):
        return str(self.id) +' : ' + self.title
