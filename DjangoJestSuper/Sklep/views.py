from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from Sklep.models import Produkt, Koszyk
from .forms import KoszykForm

# Create your views here.
def main_page(request):

    return render(request, 'Sklep/index.html')

def produkty(request):
    produkty = Produkt.objects.all()

    dane = {'produkty':produkty}

    return render(request, 'Sklep/produkty.html', dane)

def produkt(request,id):
    form = KoszykForm()
    produkt = Produkt.objects.get(pk=id)
    p_id=id
    dane = {'produkt':produkt,'p_id':p_id,'form':form}

    return render(request, 'Sklep/produkt.html', dane)

@login_required
def dodajkoszyk(request,id):
    produkt = Produkt.objects.get(pk=id)
    p_id = id
    if Koszyk.objects.filter(user= request.user,nazwa_user=produkt.nazwa).exists():
        produkt_koszyk = Koszyk.objects.get(user= request.user,nazwa_user=produkt.nazwa)
    else:
        Koszyk.objects.create(user=request.user, nazwa_user=produkt.nazwa, cena_user=produkt.cena, dodane_user=produkt.dodane)
        produkt_koszyk = Koszyk.objects.get(user=request.user, nazwa_user=produkt.nazwa)
    if request.method != 'POST':
        form = KoszykForm(instance=produkt_koszyk)
    else:
        form = KoszykForm(instance=produkt_koszyk, data=request.POST)
        if form.is_valid():
            form.save()

    dane = {'produkt': produkt,'p_id':p_id, 'form':form}
    return render(request, 'Sklep/produkt.html', dane)

@login_required
def koszyk(request):
    #produkty_koszyk = Produkt.objects.exclude(dodane="0")
    produkty_koszyk = Koszyk.objects.filter(user=request.user)
    cena = 0
    for produkt in produkty_koszyk:
        cena = cena + float(produkt.cena_user) * int(produkt.dodane_user)
        #Koszyk.objects.create()
    cena = float(round(cena, 2))
    dane = {'produkty_koszyk': produkty_koszyk, 'cena': cena}
    return render(request, 'Sklep/koszyk.html', dane)

@login_required
def kosz(request,id1,id2):
    produkt_wyb = Koszyk.objects.get(pk=id2)
    if id1 == '1':
        produkt_m = int(produkt_wyb.dodane_user) + 1
    else:
        produkt_m = int(produkt_wyb.dodane_user) - 1
    Koszyk.objects.filter(pk=id2).update(dodane_user=produkt_m)
    produkty_koszyk = Koszyk.objects.filter(user=request.user)
    cena = 0
    for produkt in produkty_koszyk:
        cena = cena + float(produkt.cena_user) * int(produkt.dodane_user)
    cena = float(round(cena, 2))

    dane = {'produkty_koszyk': produkty_koszyk, 'cena': cena}
    return render(request, 'Sklep/koszyk.html', dane)

@login_required
def wyslij(request):

    #produkty = Produkt.objects.all()
    produkty_koszyk = Koszyk.objects.filter(user=request.user)
    cena = 0

    for produkt in produkty_koszyk:
        cena = cena + float(produkt.cena_user) * int(produkt.dodane_user)

    cena = float(round(cena, 2))
    file = open(f'C:/Users/Marcin/Desktop/zamowienie_{request.user}.txt', "w")
    file.write(f"rachunek użytkownika: {request.user} \n")
    for obiekt in produkty_koszyk:
        file.write(f"nazwa: {obiekt.nazwa_user}, ilość zakupionych sztuk: {produkt.dodane_user} \n")
    file.write(f"kwota do zapłaty: {cena}")
    file.close()

    # for produkt in produkty:
    #     Produkt.objects.filter(nazwa=produkt).update(dodane="0")
    Koszyk.objects.filter(user=request.user).delete()
    produkty_koszyk = False
    cena = 0

    dane = {'produkty_koszyk': produkty_koszyk,'cena': cena}
    return render(request, 'Sklep/koszyk.html', dane)



