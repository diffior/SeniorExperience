from django.db import models

class Inventory(models.Model):
    instance_name = models.CharField(max_length=100)
    host_ip = models.GenericIPAddressField()
    user = models.CharField(max_length=100)
    ssh_key_path = models.CharField(max_length=200)
    python_interpreter = models.CharField(max_length=200)

    def to_ini(self):
        # Manually format the inventory data to INI format
        ini_content = f"""
[InventoryItem]
instance_name = {self.instance_name}
host_ip = {self.host_ip}
user = {self.user}
ssh_key_path = {self.ssh_key_path}
python_interpreter = {self.python_interpreter}
        """.strip()  # `.strip()` to remove leading and trailing newlines for neatness
        return ini_content
    
    def __str__(self):
        return self.name
