# -*- coding: utf-8 -*-
"""
różne 'helper functions' do czytania i edycji plików ini

słownik do ini ma zawsze formę:

slownik[nazwa_sekcji][nazwa_elementu]= wartosc_elementu

i to się zamieni w pliku ini na:

[nazwa sekcji]
nazwa_elementu = wartosc_elementu

"""
import configparser


def czytaj_konfig(nazwa_pliku):
    pass


def zapisz_ini_ze_slownik(slownik, nazwa_pliku):
    """zapisuje konfigurację ini na podstawie słownika

    Args:
        slownik (dict): slownik do zapisania
        nazwa_pliku (str): nazwa/ sciezka do pliku

    Slownik musi mieć formę, że dla każdego klucza,
    oznaczającego sekcję
    jest kolejny słownik zawierający poszczególne
    elementy
    
    Examples:
        >>> slownik={"Owner":{"animal":"turtle"}}
        >>> slownik["x-axis"]={"fontsize":20}
        >>> slownik["x-axis"]["where"]="top"
        >>> zapisz_konfig(slownik,"nowa_li_slownik.ini")
        plik nowa_li_slownik.ini zapisany

    """
    config = configparser.RawConfigParser()
    config.read_dict(slownik)
    config.write(open(nazwa_pliku, "w"))
    print("plik {} zapisany".format(nazwa_pliku))


def add_ini_slownik(slownik, nazwa_pliku, nowa_nazwa=None):
    """ Funkcja do pliku ini dopisuje dane ze słownika
    
    Args:
        slownik (dict): slownik z sekcjami i elementami
        nazwa_pliku (path): ścieżka do pliku ini który jest bazą do zmian
        nowa_nazwa (path): ścieżka do pliku ini który będzie wynikowym plikiem, plik opcjonalny (możemy nadpisać nazwa_pliku)
    
    Examples:
        >>> slownik_z_nowymi_rzeczami={"Lidki":{"zwierzę":"Żółw"}}
        >>> add_ini_slownik(slownik_z_nowymi_rzeczami,"testtt.ini","nowy_nowy.ini")
    """
    config = configparser.RawConfigParser()
    config.read(nazwa_pliku)
    dopisz_do_konfig(config, slownik)
    if nowa_nazwa:
        nazwa_pliku=nowa_nazwa
    
    config.write(open(nazwa_pliku,"w"))
    print("zapisano pod nazwą", nazwa_pliku)


def dopisz_do_konfig(konfig, slownik):
    """do obiektu konfig dopisuje (w miejscu) elementy ze slownika
    Args:
        konfig (configparser.RawConfigParser): obiekt zawierajacy konfigurację
        slownik (dict): slownik z sekcjami i elementami
        
    """ 
    
    for nazwa_sekcji,slownik_sekcji in slownik.items():
        
        try:
            konfig.add_section(nazwa_sekcji)
        except :
            print("sekcja {} już istniała".format(nazwa_sekcji))
        
        for nazwa_el,wartosc_el in slownik_sekcji.items():
            konfig.set(nazwa_sekcji,nazwa_el,wartosc_el)
    
