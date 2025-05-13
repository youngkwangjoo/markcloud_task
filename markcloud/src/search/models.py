from django.db import models

class Trademark(models.Model):
    productName = models.CharField(max_length=255)  
    productNameEng = models.CharField(max_length=255, blank=True, null=True) 

    applicationNumber = models.CharField(max_length=50)
    applicationDate = models.CharField(max_length=8, blank=True, null=True)

    registerStatus = models.CharField(max_length=50, blank=True, null=True)

    publicationNumber = models.CharField(max_length=50, blank=True, null=True)
    publicationDate = models.CharField(max_length=8, blank=True, null=True)

    registrationNumber = models.CharField(max_length=50, blank=True, null=True)
    registrationDate = models.CharField(max_length=8, blank=True, null=True)

    internationalRegNumbers = models.JSONField(blank=True, null=True)
    internationalRegDate = models.CharField(max_length=8, blank=True, null=True)

    priorityClaimNumList = models.JSONField(blank=True, null=True)
    priorityClaimDateList = models.JSONField(blank=True, null=True)

    asignProductMainCodeList = models.JSONField(blank=True, null=True)
    asignProductSubCodeList = models.JSONField(blank=True, null=True)
    viennaCodeList = models.JSONField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.productName or "Unnamed Trademark"
