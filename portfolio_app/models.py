from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    demo_url = models.URLField(blank=True)

    def __str__(self):
        return self.title

class Experience(models.Model):
    company = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.role} at {self.company}"

class Education(models.Model):
    institution = models.CharField(max_length=150)
    degree = models.CharField(max_length=150)
    start_year = models.IntegerField()
    end_year = models.IntegerField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)     # Existing URL for images
    image = models.ImageField(upload_to='institutes/', blank=True, null=True)  # New upload field
    description = models.TextField(blank=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.degree} from {self.institution}"

class Resume(models.Model):
    title = models.CharField(max_length=200, default="Resume")
    file = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.title

class AdditionalSection(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title
