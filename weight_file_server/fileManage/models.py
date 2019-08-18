from django.db import models

class WeightFile(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, default='no title')
    weight_file = models.FileField(blank = False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.auto_increment_id) +' : ' + self.title

    # def summary(self):
    #     return self.body[:100]