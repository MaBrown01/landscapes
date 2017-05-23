from django.shortcuts import render
import random


def isPrime(n):
    n = int(n)
    i = 2
    while(i * i <= n):
        if(n % i ==0):
            return False
        i += 1
    return n > 1
# Create your views here.
def index(request, n):
    n = int(n)
    landscapes = [

    'http://www.fantasticviewpoint.com/wp-content/uploads/2013/11/8356_winter_snow.jpgd
    'https://feel-planet.com/wp-content/uploads/2016/08/Pinnacles-WA.jpg',
    'https://s-media-cache-ak0.pinimg.com/originals/fe/a2/9e/fea29edcc91becdfbdfd575dc41aedc0.jpg',
    'http://www.vfmii.com/medlib6/VIZ_C4415490_photo/0/69/721/69721854/69721854.jpg',
    'http://1adt.com/wp-content/uploads/2015/06/most-breathtaking-tropical-photos-and-places-in-the-world-houses-on-the-beach-1adt.com_.jpgd
    'https://s-media-cache-ak0.pinimg.com/originals/4f/a3/6d/4fa36d3b93bd3f8d3971a48ed727e5a6.jpg'
    'http://eskipaper.com/images/stunning-tropical-wallpaper-1.jpg',
    'http://www.technocrazed.com/wp-content/uploads/2016/04/Bora-Bora-Island_French-Polynesia_FO-HB9STJ_DX-News.jpg',
    ]
    if n < 1 or n > 50:
        pic = random.choice(landscapes)
    if isPrime(n):
        pic = landscapes[-1]
    elif n < 11:
        pic = landscapes[0]
    elif n < 21:
        pic = landscapes[1]
    elif n < 31:
        pic = landscapes[2]
    elif n < 41:
        pic = landscapes[3]
    else:
        landscapes[4]
    context = {
    'pic': pic
    }
    return render(request, 'main/index.htmld context)
