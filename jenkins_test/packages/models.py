from django.db import models


class Package(models.Model):
    pkg_name = models.CharField(max_length=200, null=False)
    pkg_code = models.CharField(max_length=200, null=False)
    display_name = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    global_enable = models.BooleanField(default=False)
    created_ts = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pkg_name
