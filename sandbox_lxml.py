# create json file from xml keeping in mind the faulty asins

import amazon_xml_item
reload(amazon_xml_item)

from amazon_xml_item import AmazonXMLItem


xml_file_name = '/Users/susanaparis/Documents/Belgium/PARIS/Amazon/scripts/dresses/data/xml/Bridesmaid Dresses/B00LA3V9LA.xml'


axml = AmazonXMLItem(xml_file_name)

axml.get_asin()
axml.get_title()
axml.get_all_features()
axml.get_editorial()
axml.get_attributes()


axml.item.ItemAttributes.Feature
"""
['Binding',
 'Brand',
 'Color',
 'Department',
 'Feature',
 'Model',
 'ProductGroup',
 'ProductTypeName',
 'Title']"""

a = axml.item.ItemAttributes[0]

for c in a.getchildren():
    print c.tag
    print c.text


a.findall(axml.nspace + 'Feature')

for t in a.getchildren():
    print t.tag
    print t.text

for t in a.getiterator():
    print t


for t in a.iter():
    print t

a.countchildren()  # 13




# axml.item.ItemAttributes.getchildren()
# ['Apparel',
#  'Maillsa',
#  'Purple',
#  'womens',
#  'Fabric: Chiffon',
#  'Silhouette: A-Line.',
#  'Neckline:  Sweetheart',
#  'Hemline:Knee Length',
#  'ATTENTION: 1. We have our OWN size chart as shown in the product images column. The sizes are DIFFERENT from what you normally wear. Please remember to check our size chart BEFORE purchase. 2. We just offer sizes that you can choose from the drop-down menu. If you need special sizes, please ask for customization.',
#  'PP52',
#  'Apparel',
#  'DRESS',
#  '*Maillsa 2014 New Style Sweetheart Bridesmaids Chiffon Dress PP52']