from django.http import HttpResponse
from django.shortcuts import render
import pprint
from bitrix24 import *
from .models import *

class AnketaFromBitrix:
    webhook = "https://novoedelo.bitrix24.ru/rest/16/kqso8qps07ade9zb/"
    b = Bitrix24(webhook)
    fieldsDeal = {
        "Ситуация" : "UF_CRM_5F102FA7BD042",
        "Место жительства": "UF_CRM_5F0F185114F76",
        "Регион прописки" : "UF_CRM_5D1B2B8F46CB7",
        "Сумма долга" : "UF_CRM_628B3774228C2",
        "Кредиты и обязательства" : "UF_CRM_628B3754B3640",
        "Просрочки по кредитам" : "UF_CRM_628B375679F49",
        "Ежемесячный платеж по всем кредитам" : "UF_CRM_628B3758A8E8B",
        "Ближайший платёж" : "UF_CRM_628B375A90C47",
        "Имущество в данный момент" : "UF_CRM_628B375C5670C",
        "Сделки" : "UF_CRM_628B375E26B25",
        "Дети несовершеннолетние" : "UF_CRM_60D1EB78E0247",
        "Фактический доход" : "UF_CRM_628B375FBA53C",
        "Фактическая работа":"UF_CRM_628B37617B982",
        "Официальный доход НДФЛ" : "UF_CRM_628B376330E2F",
        "Логин в Госуслуги" : "UF_CRM_628B376505591",
        "Пароль для Госуслуг" : "UF_CRM_628B3766A7F11",
        "Серия и номер паспорта" : "UF_CRM_628B3768AC7CE",
        "Дата выдачи паспорта" : "UF_CRM_628B376B35639",
        "Итог" : "UF_CRM_628B376D30D4E",
        "Вариант списания" : "UF_CRM_628B3771D7FA8"
}
    fieldsLead = {
        "Ситуация": "UF_CRM_1594896052079",
        "Место жительства": "UF_CRM_1594822925",
        "Регион прописки": "UF_CRM_1561980772572",
        "Сумма долга": "UF_CRM_1653238944",
        "Кредиты и обязательства": "UF_CRM_1653232075",
        "Просрочки по кредитам": "UF_CRM_1653236732",
        "Ежемесячный платеж по всем кредитам": "UF_CRM_1653236980",
        "Ближайший платёж": "UF_CRM_1653237134",
        "Имущество в данный момент": "UF_CRM_1653237303",
        "Сделки": "UF_CRM_1653237620",
        "Дети несовершеннолетние": "UF_CRM_1624283384",
        "Фактический доход": "UF_CRM_1653238045",
        "Фактическая работа": "UF_CRM_1653238136",
        "Официальный доход НДФЛ": "UF_CRM_1653238256",
        "Логин в Госуслуги": "UF_CRM_1653238486",
        "Пароль для Госуслуг": "UF_CRM_1653238557",
        "Серия и номер паспорта": "UF_CRM_1653238594",
        "Дата выдачи паспорта": "UF_CRM_1653238642",
        "Итог": "UF_CRM_1653238683",
        "Вариант списания": "UF_CRM_1653238724"
    }
    def treatmentInfo(request,methodBitrix,check,idFromBitrix='',):
        fields = {}
        if request.POST:
            pprint.pprint(request.POST)
            if check == True:
                fields = {
                    'NAME': request.POST['Имя'],
                    'LAST_NAME': request.POST['Фамилия'],
                    'SECOND_NAME': request.POST['Отчество'],
                    'UF_CRM_1594896052079': request.POST.get('Сложное финансовое положение', ''),
                    'UF_CRM_1594822925': request.POST.get('Место фактического проживания', ''),
                    'UF_CRM_1561980772572': request.POST.get('Место регистрации', ''),
                    'UF_CRM_1653238944': request.POST.get('Сумма ВСЕХ кредитов', ''),
                    'UF_CRM_1653232075': ", ".join(
                        [item for item in request.POST.getlist('Обязательства и кредиты[]')]),
                    "UF_CRM_1653236732": request.POST.get("Просрочки по кредитам", ''),
                    "UF_CRM_1653236980": request.POST.get("Ежемесячный платёж", ''),
                    "UF_CRM_1653237134": request.POST.get("Ближайший платёж", ''),
                    "UF_CRM_1653237303": ", ".join(
                        [item for item in request.POST.getlist('Имущество в данный момент[]')]),
                    "UF_CRM_1653237620": ", ".join([item for item in request.POST.getlist('Сделки[]')]),
                    "UF_CRM_1624283384": ", ".join([item for item in request.POST.getlist('Дети[]')]),
                    "UF_CRM_1653238045": request.POST.get('Фактический доход'),
                    "UF_CRM_1653238136": request.POST.get('Фактическая работа', ''),
                    "UF_CRM_1653238256": request.POST.get('Официальный доход 2НДФЛ', ''),
                    "UF_CRM_1654862734": request.POST.get('Дата рождения', ''),
                    "UF_CRM_1653238486": request.POST.get('Логин', ''),
                    "UF_CRM_1653238557": request.POST.get('Пароль', ''),
                    "UF_CRM_1653238594": request.POST.get('Серия и номер паспорта', ''),
                    "UF_CRM_1653238642": request.POST.get('Дата выдачи папорта', ''),
                    "UF_CRM_1653238683": request.POST.get('Добиться в конечном итоге', ''),
                    "UF_CRM_1653238724": request.POST.get('Вариант списания', ''),
                    "EMAIL": request.POST.get('Email', ''),
                    "PHONE": [{ "VALUE": f"{request.POST.get('phone', '')}", "VALUE_TYPE": "WORK" }],
                    "UF_CRM_1624284141": request.POST.get('Семейное положение', ''),
                }
            else:
                fields = {
                    'UF_CRM_NAME': request.POST['Имя'],
                    'UF_CRM_LAST_NAME': request.POST['Фамилия'],
                    'UF_CRM_SECOND_NAME': request.POST['Отчество'],
                    'UF_CRM_5F102FA7BD042': request.POST.get('Сложное финансовое положение', ''),
                    'UF_CRM_5F0F185114F76': request.POST.get('Место фактического проживания', ''),
                    'UF_CRM_5D1B2B8F46CB7': request.POST.get('Место регистрации', ''),
                    'UF_CRM_628B3774228C2': request.POST.get('Сумма ВСЕХ кредитов', ''),
                    'UF_CRM_628B3754B3640': ", ".join(
                        [item for item in request.POST.getlist('Обязательства и кредиты[]')]),
                    "UF_CRM_628B375679F49": request.POST.get("Просрочки по кредитам", ''),
                    "UF_CRM_628B3758A8E8B": request.POST.get("Ежемесячный платёж", ''),
                    "UF_CRM_628B375A90C47": request.POST.get("Ближайший платёж", ''),
                    "UF_CRM_628B375C5670C": ", ".join(
                        [item for item in request.POST.getlist('Имущество в данный момент[]')]),
                    "UF_CRM_628B375E26B25": ", ".join([item for item in request.POST.getlist('Сделки[]')]),
                    "UF_CRM_60D1EB78E0247": ", ".join([item for item in request.POST.getlist('Дети[]')]),
                    "UF_CRM_628B375FBA53C": request.POST.get('Фактический доход'),
                    "UF_CRM_628B37617B982": request.POST.get('Фактическая работа', ''),
                    "UF_CRM_628B376330E2F": request.POST.get('Официальный доход 2НДФЛ', ''),
                    "UF_CRM_1654862734": request.POST.get('Дата рождения', ''),
                    "UF_CRM_628B376505591": request.POST.get('Логин', ''),
                    "UF_CRM_628B3766A7F11": request.POST.get('Пароль', ''),
                    "UF_CRM_628B3768AC7CE": request.POST.get('Серия и номер паспорта', ''),
                    "UF_CRM_628B376B35639": request.POST.get('Дата выдачи папорта', ''),
                    "UF_CRM_628B376D30D4E": request.POST.get('Добиться в конечном итоге', ''),
                    "UF_CRM_628B3771D7FA8": request.POST.get('Вариант списания', ''),
                    "EMAIL": request.POST.get('Email', ''),
                    "PHONE": [{ "VALUE": f"{request.POST.get('phone', '')}", "VALUE_TYPE": "WORK" }],
                    "UF_CRM_6006C55D9ADFA": request.POST.get('Семейное положение', '')
                }

            if idFromBitrix == '':
                add = AnketaFromBitrix.b.callMethod(methodBitrix, fields=fields)
            else:
                update = AnketaFromBitrix.b.callMethod(methodBitrix, ID=idFromBitrix, fields=fields)
            return True


    def leadPage(request,idFromBitrix):
        checkIsLead = True
        updateLead = 'crm.lead.update'
        region = PlaceOfRegistrationForLead.objects.all()
        mesto = PlaceOfResidenceForLead.objects.all()
        AnketaFromBitrix.treatmentInfo(request,methodBitrix=updateLead,idFromBitrix=idFromBitrix,check=checkIsLead)
        return render(request, "anketaPage/anketa.html",{"region":region,"mesto":mesto})

    def dealPage(request,idFromBitrix):
        region = PlaceOfRegistrationForDeal.objects.all()
        mesto = PlaceOfResidenceForDeal.objects.all()
        checkIsLead = False
        updateDeal = 'crm.deal.update'
        AnketaFromBitrix.treatmentInfo(request,methodBitrix=updateDeal,idFromBitrix=idFromBitrix,check=checkIsLead)
        return render(request, "anketaPage/anketa.html",{"region":region,"mesto":mesto})

    def indexPage(request):
        region = PlaceOfRegistrationForLead.objects.all()
        mesto = PlaceOfResidenceForLead.objects.all()
        # update = AnketaFromBitrix.b.callMethod('crm.deal.get', ID=28070)
        # print(update['UF_CRM_5F0F185114F76'])
        checkIsLead = True
        addLead = 'crm.lead.add'
        AnketaFromBitrix.treatmentInfo(request,methodBitrix=addLead,check=checkIsLead)
        return render(request, "anketaPage/anketa.html",{"region":region,"mesto":mesto})


