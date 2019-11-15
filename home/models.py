from django.db import models


class Office(models.Model):
    officecode = models.CharField(max_length=50, primary_key=True)
    officename = models.CharField(max_length=50)
    attribution = models.CharField(max_length=50)

class Organization(models.Model):
    organization_code = models.CharField(max_length=50, primary_key=True)
    organization_name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    date_joined = models.CharField(max_length=50)
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)           

class Service(models.Model):
    servicecode = models.CharField(max_length=50, primary_key=True)
    servicename = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    premium = models.CharField(max_length=50)
    allocation = models.CharField(max_length=50)


class SubscriptionType(models.Model):
    subscriptiontypecode = models.CharField(max_length=50, primary_key=True)
    subscriptiontypename = models.CharField(max_length=50)

class UserInfo(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    first_name= models.CharField(max_length=50)
    middlename = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    employer_name = models.CharField(max_length=50)


class Subscriber(models.Model):
    requestdate = models.CharField(max_length=50)
    startdate = models.CharField(max_length=50)
    enddate = models.CharField(max_length=50)
    motifofcancellation = models.CharField(max_length=50)
    beneficiaryID = models.CharField(max_length=50)
    subscriberID = models.CharField(max_length=50, primary_key=True)
    username = models.ForeignKey(
        UserInfo,
        on_delete=models.CASCADE
    )
    subscriptiontypecode = models.ForeignKey(
        SubscriptionType,
        on_delete=models.CASCADE
    )
    servicecode = models.ForeignKey(
        Service,
        on_delete=models.CASCADE
    )


class TransferredSubscription(models.Model):
    transfer_fromm = models.CharField(max_length=50, primary_key=True)
    transfer_to = models.CharField(max_length=50)
    request_date = models.CharField(max_length=50)
    transfer_date = models.CharField(max_length=50)
    subscriberID = models.ForeignKey(
        Subscriber,
        on_delete=models.CASCADE
    )



class Officer(models.Model):
    officecode = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE
        )
    subscriberID = models.ForeignKey(
        Office,
        on_delete=models.CASCADE
        )
    startdate = models.CharField(max_length=50)
    enddate = models.CharField(max_length=50)


class OrganizationMember(models.Model):
    organization_code = models.ForeignKey(Organization, 
        on_delete=models.CASCADE
	)
    subscriberID = models.ForeignKey(
        Subscriber, 
        on_delete=models.CASCADE
        )
    startdate = models.CharField(max_length=50)
    enddate = models.CharField(max_length=50)
    nativecountry = models.CharField(max_length=50)
    citizenship = models.CharField(max_length=50)
    isdelegate = models.CharField(max_length=50)

