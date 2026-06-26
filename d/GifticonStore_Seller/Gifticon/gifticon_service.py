from Gifticon.gifticon import Gifticon

class GifticonService:
    def __init__(self, gifticon_dao):
        self.dao = gifticon_dao

    def get_all_gifticons(self):
        return self.dao.select_all_gifticons()

    def get_gifticon(self, gifticon_no):
        return self.dao.select_gifticon_by_no(gifticon_no)

    def get_seller_gifticons(self, seller_id):
        return self.dao.select_gifticons_by_seller(seller_id)

    def add_gifticon(self, seller_id, name, brand, category, price, stock):
        if int(price) <= 0 or int(stock) < 0:
            raise ValueError('가격은 1원 이상, 재고는 0개 이상이어야 합니다')
        gifticon_no = self.dao.next_no()
        gifticon = Gifticon(gifticon_no, seller_id, name, brand, category, price, stock)
        return self.dao.insert_gifticon(gifticon)

    def update_gifticon_info(self, gifticon_no, seller_id, select, value):
        gifticon = self.dao.select_gifticon_by_no(gifticon_no)
        if not gifticon:
            return False
        if seller_id != 'admin' and gifticon.get_seller_id() != seller_id:
            raise PermissionError('본인이 등록한 기프티콘만 수정할 수 있습니다')
        if select == 1:
            gifticon.set_price(value)
        elif select == 2:
            gifticon.set_stock(value)
        elif select == 3:
            gifticon.set_name(value)
        else:
            return False
        return self.dao.update_gifticon(gifticon_no, gifticon)

    def delete_gifticon(self, gifticon_no, seller_id):
        gifticon = self.dao.select_gifticon_by_no(gifticon_no)
        if not gifticon:
            return False
        if seller_id != 'admin' and gifticon.get_seller_id() != seller_id:
            raise PermissionError('본인이 등록한 기프티콘만 삭제할 수 있습니다')
        return self.dao.delete_gifticon(gifticon_no)
