from django.db import models

class Joint(models.Model):
    class Meta:
        verbose_name_plural='ジョイント'
    name = models.CharField(
            verbose_name='ジョイントネーム',
            blank=False,
            null=False,
            max_length=200,
            )
    description = models.TextField(
            verbose_name='ジョイント詳細',
            blank=True,
            null=True,
            )
    is_active = models.BooleanField(
            verbose_name='Active',
            default=True,
            )
    created_at = models.DateTimeField(
            verbose_name='作成日時',
            auto_now_add=True,
            )
    updated_at = models.DateTimeField(
            verbose_name='更新日時',
            auto_now_add=True,
            )
    def __int__(self):
        return self.name

class Music(models.Model):
    class Meta:
        verbose_name_plural='ミュージック'
    joint = models.ForeignKey(
            'Joint',
            verbose_name='ジョイント',
            on_delete=models.CASCADE
          )
    name = models.CharField(
            verbose_name='曲名',
            blank=False,
            null=False,
            max_length=200,
            )
    description = models.TextField(
            verbose_name='ミュージック詳細',
            blank=True,
            null=True,
            )
    url = models.CharField(
            verbose_name='URL',
            blank=False,
            null=False,
            max_length=200,
            )
    is_played = models.BooleanField(
            verbose_name='再生済',
            default=False,
            )
    is_active = models.BooleanField(
            verbose_name='Active',
            default=True,
            )
    created_at = models.DateTimeField(
            verbose_name='作成日時',
            auto_now_add=True,
            )
    updated_at = models.DateTimeField(
            verbose_name='更新日時',
            auto_now_add=True,
            )
