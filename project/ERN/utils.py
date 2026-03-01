from django.core.cache import cache
from . import models
class Helpers:
    Normal_Relic_Url = 'img/NormalRelic/'
    Cursed_Relic_Url = 'img/CursedRelic/'
    Relics_Adress_Icons = {
        'BIG_RED': Normal_Relic_Url + 'BigRed.jpg',
        'BIG_GREEN': Normal_Relic_Url + 'BigGreen.jpg',
        'BIG_YELLOW': Normal_Relic_Url + 'BigYellow.jpg',
        'BIG_BLUE': Normal_Relic_Url + 'BigBlue.jpg',
        'SMALL_BLUE': Normal_Relic_Url + 'SmallBlue.jpg',
        'SMALL_YELLOW': Normal_Relic_Url + 'SmallYellow.jpg',
        'SMALL_GREEN': Normal_Relic_Url + 'SmallGreen.jpg',
        'SMALL_RED': Normal_Relic_Url + 'SmallRed.jpg',
        'MEDIUM_BLUE': Normal_Relic_Url + 'MediumBlue.jpg',
        'MEDIUM_YELLOW': Normal_Relic_Url + 'MediumYellow.jpg',
        'MEDIUM_GREEN': Normal_Relic_Url + 'MediumGreen.jpg',
        'MEDIUM_RED': Normal_Relic_Url + 'MediumRed.jpg',
        'CURSED_YELLOW':Cursed_Relic_Url + 'CursedYellow.jpg',
        'CURSED_GREEN': Cursed_Relic_Url + 'CursedGreen.jpg',
        'CURSED_RED':Cursed_Relic_Url + 'CursedRed.jpg',
        'CURSED_BLUE':Cursed_Relic_Url + 'CursedBlue.jpg',
        'CURSED_MEDIUM_YELLOW':Cursed_Relic_Url + 'CursedMediumYellow.jpg',
        'CURSED_MEDIUM_BLUE':Cursed_Relic_Url + 'CursedMediumBlue.jpg',
        'CURSED_MEDIUM_RED':Cursed_Relic_Url + 'CursedMediumRed.jpg',
        'CURSED_MEDIUM_Green':Cursed_Relic_Url + 'CursedMediumGreen.jpg',
        'CURSED_BIG_YELLOW':Cursed_Relic_Url + 'CursedBigYellow.jpg',
        'CURSED_BIG_BLUE':Cursed_Relic_Url + 'CursedBigBlue.jpg',
        'CURSED_BIG_RED':Cursed_Relic_Url + 'CursedBigRed.jpg',
        'CURSED_BIG_GREEN':Cursed_Relic_Url + 'CursedBigGreen.jpg',
    }

    @classmethod
    def get_relic_icon(cls,relic_type):    
        return cls.Relics_Adress_Icons.get(relic_type)
    
    @classmethod
    def get_all_icons(cls):
        return cls.Relics_Adress_Icons

    @classmethod
    def get_relic_icon_cached(cls, relic_type):
        cache_key = f'relic_icon_{relic_type}'
        icon_url = cache.get(cache_key)
        
        if not icon_url:
            icon_url = cls.get_relic_icon_url(relic_type)
            cache.set(cache_key, icon_url, 3600)  #cached 1 hour
            
        return icon_url