from django.shortcuts import render, redirect  
from musicdatab.forms import MusicianForm , AlbumForm ,InstrumentForm, Full_AddressForm , SongForm, PerformanceForm,Instrument_PlayerForm
from musicdatab.models import Musician  , Instrument,Instrument_Player, Song, Performance,Full_Address
from musicdatab.models import Album   

def home(request):
    return render(request,"home.html")

def show(request):  
    musicians = Musician.objects.all()  
    albums = Album.objects.all()
    return render(request,"show.html",{
        'musicians':musicians,
        'albums': albums,
    }) 



def showall(request):
    musicians = Musician.objects.all()  
    albums = Album.objects.all() 
    instruments = Instrument.objects.all()  
    instrument_players = Instrument_Player.objects.all()  
    songs = Song.objects.all()  
    full_addresss = Full_Address.objects.all()  
    performances = Performance.objects.all() 


    return render(request,"showall.html",{
        'musicians':musicians,
        'albums': albums,
        'instruments':instruments,
        'instrument_players':instrument_players,
        'songs':songs,
        'full_addresss':full_addresss,
        'performances':performances,
       
    })

def user(request):
    return render(request,"user.html")
