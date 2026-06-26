class CartDAO:
    def __init__(self):
        self.__cart_db = {}  # member_id : {gifticon_no : CartItem}

    def select_cart(self, member_id):
        return list(self.__cart_db.get(member_id, {}).values())

    def insert_or_update_item(self, item):
        cart = self.__cart_db.setdefault(item.member_id, {})
        if item.gifticon_no in cart:
            cart[item.gifticon_no].quantity += item.quantity
        else:
            cart[item.gifticon_no] = item
        return True

    def delete_item(self, member_id, gifticon_no):
        cart = self.__cart_db.get(member_id, {})
        gifticon_no = str(gifticon_no)
        if gifticon_no not in cart:
            return False
        del cart[gifticon_no]
        return True

    def clear_cart(self, member_id):
        self.__cart_db[member_id] = {}
        return True
