from django.db import models


class SingletonModel(models.Model):
    INSTANCE_ID = 1

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = SingletonModel.INSTANCE_ID
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        return cls.objects.get_or_create(pk=cls.INSTANCE_ID)[0]
