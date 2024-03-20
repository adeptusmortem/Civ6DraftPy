class LeaderClass:

    #атрибуты лидеров, имя, специализация, нация, можно будет добавить еще роль и тд
    def __init__(self, name, spec, nation):
        self.name = name      # имя лидера
        self.spec = spec      # специализация лидера
        self.nation = nation  # нация
       
    #прекол для сериализации
    def to_dict(self):
        return self.__dict__
        
        
#прекол для сериализации
def class_to_dict(obj):
    return obj.__dict__

import json

def GenerateNations():
    nations = []
    nations.append(LeaderClass('Пётр Великий','','Россия'))
    nations.append(LeaderClass('Алиенора Аквитанская','','Англия'))
    nations.append(LeaderClass('Алиенора Аквитанская','','Франция'))
    nations.append(LeaderClass('Виктория','Эпоха паровых машин','Англия'))
    nations.append(LeaderClass('Виктория','Эпоха империи','Англия'))
    nations.append(LeaderClass('Елизавета I','','Англия'))
    nations.append(LeaderClass('Екатерина Медичи','Великолепная','Франция'))
    nations.append(LeaderClass('Екатерина Медичи','Черная вдова','Франция'))
    nations.append(LeaderClass('Траян','','Рим'))
    nations.append(LeaderClass('Юлий Цезарь','','Рим'))
    nations.append(LeaderClass('Фридрих Барбаросса','','Германия'))
    nations.append(LeaderClass('Людвиг II','','Германия'))
    nations.append(LeaderClass('Теодор Рузвельт','Прогрессивист','Америка'))
    nations.append(LeaderClass('Теодор Рузвельт','Мужественный всадник','Америка'))
    nations.append(LeaderClass('Авраам Линкольн','','Америка'))
    nations.append(LeaderClass('Ганди','','Индия'))
    nations.append(LeaderClass('Чандрагупта','','Индия'))
    nations.append(LeaderClass('Томирис','','Скифия'))
    nations.append(LeaderClass('Перикл','','Греция'))
    nations.append(LeaderClass('Горго','','Греция'))
    nations.append(LeaderClass('Цинь Шихуанди','Небесный мандат','Китай'))
    nations.append(LeaderClass('Цинь Шихуанди','Освободитель','Китай'))
    nations.append(LeaderClass('Юнлэ','','Китай'))
    nations.append(LeaderClass('У Цзэтянь','','Китай'))
    nations.append(LeaderClass('Хубилай','','Китай'))
    nations.append(LeaderClass('Хубилай','','Монголия'))
    nations.append(LeaderClass('Рамсес II','','Египет'))
    nations.append(LeaderClass('Клеопатра','Египет','Египет'))
    nations.append(LeaderClass('Клеопатра','Династия Птолемеев','Египет'))
    nations.append(LeaderClass('Монтесума','','Ацтеки'))
    nations.append(LeaderClass('Педру II','','Бразилия'))
    nations.append(LeaderClass('Филипп II','','Испания'))
    nations.append(LeaderClass('Ходзё Токимунэ','','Япония'))
    nations.append(LeaderClass('Токугава','','Япония'))
    nations.append(LeaderClass('Мвемба а Нзинга','','Конго'))
    nations.append(LeaderClass('НЗинга Мбанди','','Конго'))
    nations.append(LeaderClass('Саладин','Визирь','Аравия'))
    nations.append(LeaderClass('Саладин','Султан','Аравия'))
    nations.append(LeaderClass('Харальд Суровый','Конуг','Норвегия'))
    nations.append(LeaderClass('Харальд Суровый','Варяг','Норвегия'))
    nations.append(LeaderClass('Гильгамеш','','Шумер'))
    nations.append(LeaderClass('Ядвига','','Польша'))
    nations.append(LeaderClass('Джон Кэртин','','Австралия'))
    nations.append(LeaderClass('Кир','','Персия'))
    nations.append(LeaderClass('Надир-шах','','Персия'))
    nations.append(LeaderClass('Александр','','Македония'))
    nations.append(LeaderClass('Аманиторе','','Нубия'))
    nations.append(LeaderClass('Трибхувана','','Индонезия'))
    nations.append(LeaderClass('Джайаварман VII','','Кхемры'))
    nations.append(LeaderClass('Сондок','','Корея'))
    nations.append(LeaderClass('Седжон','','Корея'))
    nations.append(LeaderClass('Вильгельмина','','Нидерланды'))
    nations.append(LeaderClass('Чингисхан','','Монголия'))
    nations.append(LeaderClass('Паундмейкер','','Кри'))
    nations.append(LeaderClass('Тамара','','Грузия'))
    nations.append(LeaderClass('Роберт Брюс','','Шотландия'))
    nations.append(LeaderClass('Лаутаро','','Мапуче'))
    nations.append(LeaderClass('Чака','','Зулусы'))
    nations.append(LeaderClass('Матьяш I','','Венгрия'))
    nations.append(LeaderClass('Купе','','Маори'))
    nations.append(LeaderClass('Уилфрид Лорье','','Канада'))
    nations.append(LeaderClass('Пачакутек','','Инки'))
    nations.append(LeaderClass('Манса Муса','','Мали'))
    nations.append(LeaderClass('Сундиата Кейта','','Мали'))
    nations.append(LeaderClass('Кристина','','Швеция'))
    nations.append(LeaderClass('Сулейман','Великолепный','Османы'))
    nations.append(LeaderClass('Сулейман','Кануни','Османы'))
    nations.append(LeaderClass('Дидона','','Финикия'))
    nations.append(LeaderClass('Иш-Вак-Чан-Ахав','','Майа'))
    nations.append(LeaderClass('Симон Боливар','','Великая Колумбия'))
    nations.append(LeaderClass('Менелик II','','Эфиопия'))
    nations.append(LeaderClass('Василий II','','Византия'))
    nations.append(LeaderClass('Амбиорикс','','Галлия'))
    nations.append(LeaderClass('Хаммурапи','','Вавилон'))
    nations.append(LeaderClass('Феодора','','Вавилон'))
    nations.append(LeaderClass('Чьеу Тхи Чинь','','Вьетнам'))
    nations.append(LeaderClass('Жуан III','','Португалия'))


    with open('nations.json', 'w') as f:
        json.dump(obj=nations, fp=f, default=class_to_dict, ensure_ascii=False)