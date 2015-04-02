

from lxml import objectify

class AmazonXMLItem(object):
    def __init__(self, xml_file_name):
        """
        item is an lml object returned from reading
        and objectifying the xml file already saved
        """
        self.item = objectify.parse(xml_file_name).getroot()
        # item is an lxml object returned from the api.item_search
        #self.asin = item.ASIN.text
        self.nspace = '{' + self.item.nsmap.values()[0] + '}'

        self.image_xpath = "./{}LargeImage/{}URL".format(self.nspace, self.nspace)


    def get_asin(self):
        return self.item.ASIN.text

    def get_img_url(self):
        self.image_url = ''
        if self.item.find(self.image_xpath):
            self.image_url = self.item.find(self.image_xpath).text
        return self.image_url


    def get_title(self):
        title = ''
        if 'ItemAttributes' in dir(self.item):
            title = self.item.ItemAttributes.Title.text
        return title

    def get_editorial(self):
        editorial = ''
        if 'EditorialReviews' in dir(self.item):
            if self.item.EditorialReviews.EditorialReview.Content.text:
                editorial = self.item.EditorialReviews.EditorialReview.Content.text
        return editorial

    def get_attributes(self):
        attributes = {}
        if 'ItemAttributes' in dir(self.item):
            attribute_element = self.item.ItemAttributes[0]
            for c in attribute_element.getchildren():
                tag = c.tag.replace(self.nspace, '')
                # title, color, brand and feature are separate
                if tag == 'Title' or tag == 'Feature' or tag == 'Color' or tag == 'Brand':
                    continue
                text = c.text
                if tag not in attributes:
                    attributes[tag] = []
                attributes[tag].append(text)
        return attributes

    def get_all_features(self):
        features = []
        attribute_element = self.item.ItemAttributes[0]
        if 'Feature' in dir(attribute_element):
            features = attribute_element.findall(self.nspace + 'Feature')
            features = [f.text for f in features]
        return features

    def get_brand(self):
        brand = ''
        attribute_element = self.item.ItemAttributes[0]
        if 'Brand' in dir(attribute_element):
            brand = attribute_element.Brand.text
        return brand

    def get_color(self):
        color = ''
        attribute_element = self.item.ItemAttributes[0]
        if 'Color' in dir(attribute_element):
            color = attribute_element.Color.text
        return color



if __name__ == '__main__':


    xml_file_name = '/Users/susanaparis/Documents/Belgium/PARIS/Amazon/scripts/dresses/data/xml/Bridesmaid Dresses/B00LA3V9LA.xml'

    axml = AmazonXMLItem(xml_file_name)

    print 'asin:', axml.get_asin(), '\n'
    print 'url:', axml.get_img_url(), '\n'
    print 'title:', axml.get_title(), '\n'
    print 'features:', axml.get_all_features(), '\n'
    print 'editorial:', axml.get_editorial(), '\n'
    print 'attributes:', axml.get_attributes(), '\n'
    print 'brand:', axml.get_brand(), '\n'
    print 'color:', axml.get_color(), '\n'


