from django.db import models

class Contact(models.Model):
    INQUIRY_CHOICES = [
        ('custom-build', 'Custom Bike Build'),
        ('restoration', 'Vintage Restoration'),
        ('tuning', 'Engine Tuning & Maintenance'),
        ('parts', 'Sourcing Rare Parts'),
        ('general', 'General Question'),
    ]

    name = models.CharField(max_length=122)
    email = models.EmailField(max_length=122)
    phone = models.CharField(max_length=20, blank=True, null=True)
    inquiry_type = models.CharField(max_length=50, choices=INQUIRY_CHOICES, default='custom-build')
    bike_details = models.CharField(max_length=150, blank=True, null=True)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.get_inquiry_type_display()}"