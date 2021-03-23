import datetime
import calendar
import locale

def cyfra_dnia_tygodnia(numer):
    dni_tygodnia = ['poniedzialek','wtorek', 'środa',
                    'czwartek', 'piątek','sobota', 'niedziela']
    return dni_tygodnia[numer - 1]
    
def dzien_tygodnia_data (rok, miesiac, dzien):
    locale.setlocale(locale.LC_ALL, 'pl_pl')
    
    dzien_tygodnia = calendar.weekday (int(rok), int(miesiac), int(dzien))
    return calendar.day_name [dzien_tygodnia]

    
