from django.db import models  

class Full_Address(models.Model):
    Phone_Num = models.IntegerField("Phone Number:")
    City = models.CharField("City Name",max_length = 20)
    Area = models.CharField("Area",max_length=20)
    Street = models.CharField("Street",max_length=20)
    House_Num = models.CharField("House Number",max_length=20)

    class Meta:
        db_table ="full_address"
    def __str__(self):
        return f"Phone Number :{self.Phone_Num}"
        return f"City :{self.City}"
        return f"Area :{self.Area}"
        return f"Street :{self.Street}"
        return f"House Number :{self.House_Num}"


class Musician(models.Model):  
    M_Sn = models.IntegerField() 
    First_Name = models.CharField(max_length=100)
    Mid_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Phone_Num = models.ForeignKey(Full_Address,on_delete=models.CASCADE,default=123)

    class Meta:  
        db_table = "musician" 
    def __str__(self):
            return f"Social Security Number :{self.M_Sn}" 
            return f"First Name :{self.First_Name}" 
            return f"Mid Name :{self.Mid_Name}"
            return f"Last Name :{self.Last_Name}"
            return f"Phone Number :{self.Phone_Num}" 


class Album(models.Model):
    Title = models.CharField("Title",max_length=20)
    Alubm_ID = models.IntegerField()
    Copyright_Data = models.CharField(max_length=100)
    Format = models.CharField(max_length=100)
    class Meta:
        db_table = "album"
    def __str__(self):
            return f"Name :{self.Title}"
            return self.Alubm_ID
            return self.Format
            return f"Copyright Data :{self.Copyright_Data}"
    


class Song(models.Model):
    Title = models.CharField(max_length=100)
    Song_ID = models.IntegerField()
    Author = models.CharField(max_length=100)
    Album_ID = models.ForeignKey(Album, on_delete=models.CASCADE)

    class Meta:
        db_table = "song"
    def __str__(self):
            return f"Title :{self.Title}" 
            return f"Album ID :{self.Album_ID}" 
            return f"Author Name :{self.Author}" 
            return F"Song ID :{self.Song_ID}"





class Performance(models.Model):
    Song_ID = models.IntegerField()
    M_Sn = models.IntegerField()
    class Meta:
        db_table = "performance" 
    def __str__(self):
            return f"SSN :{self.M_Sn}" 
            return f"title name :{self.Song_ID}" 
            

class Instrument(models.Model):
    Instrument_ID = models.IntegerField()
    Music_Key=models.CharField(max_length=10)
    Name=models.CharField(max_length=30)
    class Meta:
        db_table = "instrument" 
    def __str__(self):
            return f"Instruments Name :{self.Name}" 
            return f"Music Key :{self.Music_Key}" 
            return f"Instrument ID:{self.Instrument_ID}"
            

class Instrument_Player(models.Model):
    M_Sn = models.IntegerField()
    Instrument_ID = models.IntegerField()
    class Meta:
        db_table = "instrument_player"
    def __str__(self):
            return f"Social Security Number :{self.M_Sn}" 
            return f"Instrument ID :{self.Insturment_ID}" 

