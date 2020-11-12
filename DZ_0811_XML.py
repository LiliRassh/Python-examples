import xml.etree.ElementTree as ET

'''Выбранные пользователем покупки сохраняются в XML-файлах.
Структуру XML-файла выбирайте самостоятельно.'''


class BuilderXml:

    def __init__(self, order_date, order_number):
        self.date = order_date
        self.order_id = order_number

    def add_root(self):
        root = ET.Element('NetShopPurchaseOrder', {'OrderDate': self.date, 'OrderNumber': self.order_id})
        order_items = ET.Element('OrderItems')
        root.append(order_items)
        return root

    def add_children(self, root, product_id, product_name, quantity, price):
        items = ET.SubElement(root, 'Item', {'Number': product_id})
        c1 = ET.SubElement(items, 'Product_name')
        c1.text = product_name
        c2 = ET.SubElement(items, 'Quantity')
        c2.text = quantity
        c3 = ET.SubElement(items, 'Price')
        c3.text = price

    def create_xml(self, file_xml, product_id, product_name, quantity, price):
        root = self.add_root()
        self.add_children(root[0], product_id, product_name, quantity, price)
        tree = ET.ElementTree(root)
        tree.write(file_xml)

    def edit_xml(self, file_xml, product_id, product_name, quantity, price):
        tree = ET.ElementTree(file=file_xml)
        root = tree.getroot()
        self.add_children(root[0], product_id, product_name, quantity, price)
        tree = ET.ElementTree(root)
        tree.write(file_xml)


if __name__ == "__main__":

    new_xml = BuilderXml('20191011', '1')
    new_xml.create_xml("NetShopOrder.xml", '5', 'product_5', '2', '145.5')
    new_xml.edit_xml("NetShopOrder.xml", '7', 'product_7', '1', '120')
    new_xml.edit_xml("NetShopOrder.xml", '4', 'product_4', '5', '15')


