from django.db import models


# Create your models here.
class Files_Info(models.Model):
    id = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=255, db_index=True)
    md5_fn = models.CharField(max_length=64, default="")
    ip_address = models.GenericIPAddressField(protocol="both", default="127.0.0.1")
    machine_code = models.CharField(max_length=255, default="")
    create_dt = models.DateTimeField(auto_now_add=True)
    downloads = models.IntegerField(default=0)
    state = models.BooleanField(default=True)

    class Meta:
        db_table = "files_info"
