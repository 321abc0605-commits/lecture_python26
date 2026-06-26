from Gifticon.gifticon import Gifticon

class GifticonDAO:
    def __init__(self):
        self.__gifticon_db = {}
        self.__sequence = 100
        self.insert_gifticon(Gifticon(self.next_no(), 'seller', '아메리카노 Tall', '스타벅스', '카페', 4500, 20))
        self.insert_gifticon(Gifticon(self.next_no(), 'seller', '황금올리브 치킨', 'BBQ', '치킨', 23000, 10))
        self.insert_gifticon(Gifticon(self.next_no(), 'seller', '싱글킹 아이스크림', '배스킨라빈스', '디저트', 4700, 15))

    def next_no(self):
        self.__sequence += 1
        return str(self.__sequence)

    def insert_gifticon(self, gifticon):
        gifticon_no = gifticon.get_gifticon_no()
        if gifticon_no in self.__gifticon_db:
            return False
        self.__gifticon_db[gifticon_no] = gifticon
        return True

    def select_gifticon_by_no(self, gifticon_no):
        return self.__gifticon_db.get(str(gifticon_no))

    def select_all_gifticons(self):
        gifticons = list(self.__gifticon_db.values())
        return gifticons if gifticons else None

    def select_gifticons_by_seller(self, seller_id):
        gifticons = [g for g in self.__gifticon_db.values() if g.get_seller_id() == seller_id]
        return gifticons if gifticons else None

    def update_gifticon(self, gifticon_no, gifticon):
        gifticon_no = str(gifticon_no)
        if gifticon_no not in self.__gifticon_db:
            return False
        self.__gifticon_db[gifticon_no] = gifticon
        return True

    def delete_gifticon(self, gifticon_no):
        gifticon_no = str(gifticon_no)
        if gifticon_no not in self.__gifticon_db:
            return False
        del self.__gifticon_db[gifticon_no]
        return True
