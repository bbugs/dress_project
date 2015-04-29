"""
Run this script to correct the sets of excluded or included sentences

There are two lists of errors
"""


#Rectify Included (remove from included and add to excluded)
#to exclude in second pass cause included by acciden

e = ['- Size: S, M, L',
      'Net Weight: 1.0KG',
      'Swanmate is a luxury wedding dresses and event dresses brand registered in USA.',
      'UK10 Bust33.1" Waist27.2" Hip36.2" Length35.0"',
      '- SEE MORE AND USE DISCOUNT CODE "$15OFF" AT shoplume.com',
      '24 inch long jacket.Dresses may not be returned if the original tags are removed',
      '58 inches to finished hem line.',
      '?Sora, Im glad I ran into you.?',
      'A Free Hat  &  Purse will be added to your Purchase.',
      'Garment Hip Measurement (inches): XS: 37.5, S: 39.5, M: 41.5, L: 44, XL: 47',
      'Gown runs right with size chart to the left.',
      'Lengh: S:93cm/36.6";M:94.5cm/37.2";L:96cm/37.8";XL:97.5cm/38.4" ;XXL:100CM',
      'If we dont get your height within 2 days we will make the height for S-160cm, M-165cm, L-170cm, XL-173cm.',
      'More High Quality  &  Affordable China Handmade Dresses Please Click in or Search  Dresstells !   For your accurate size choose, please refer to the Size Chart images next to the main product .Pleasse don not use other size chart!',
      'Hand or Machine Wash',
      'Please wash separately, hand wash or dry clean only',
      'Shoulder seam to hem measures approx 165 cm in length.',
      'The George Bride brand enjoys a global customer base, substantiating George Brides world-wide popularity.  George Bride team strives to offer you quality dresses at reasonable prices, in addition to exemplary customer service.',
      'The back slit length of size 6-18 are all 20-23cm',
      'The fast, flexible supply chain, together with the winning formula of style, quality, value and service has enabled sheinside to grow rapidly into a super international retailer.',
      'To be sure dresss size must be suitable for you,pls email us your chest,waist,hips size,height,weight  &  tell us when you need the dress after you order it.',
      'If you can not sure your right size according our size shart, you can send us your measurement details as list.',
      'Yacun size 10= US size 4',
      '38" length (in size 8).',
      '38" measurement from shoulder.',
      '40 1/2" (102.87 cm) in total length',
      '5.Shipped by fast shipping way, Like DHL or other fast shipping way.',
      'Can also be made in other colors of your choice',
      'Can be dry cleaned',
      'Chest: 32 inches.',
      'Color: custom made; Size: custom made (Detailed Bust__inch, Waist__inch, Hips__inch).',
      'Dry clean or machine wash cold, tumble dry low.',
      'MSRP:$430.00  Made in china',
      'Meticulous shipping prepared the same day of your order (working days), shipped from France and delivered within 6 to 8 days (working days).',
      'OSY''s offers a great assortment of styles and sizes,you''ll definitely find the best fit.',
      'Please refer to our size chart before placing the order',
      'Rinse wash.']

#########
# Rectify excluded (remove from excluded and add to included)

i = ['Sold EXCLUSIVELY by Fiesta Formals in Utah, this gorgeous long prom gown is ON SALE NOW at BELOW WHOLESALE!',
     'Sold EXCLUSIVELY by Fiesta Formals in Utah, this stunning long Fiesta Formals evening gown is ON SALE NOW for a limited time only at BELOW WHOLESALE!',
     'Short length and about 4 inches above the knee.',
     'Oversize big bowknot on the waist',
     'Peplum hem; 35.5 inch length (size S)',
     'One of the design goals is to display the buyers or the users happy feeling while a red-letter day happens to her, so we use the color red.',
     'Machine washable.It is below the knee dresses(midi dress)',
     'Machine wash only, do not bleach and cool iron if necessary,Great Everyday Dress,This tunic dress is flattering on all body types,,,',
     'A CLASSY FLORAL SWING PARTY DRESS SUITABLE FOR ALL OCCASIONS BROUGHT TO YOU BY LINDY BOP.',
     'Dress length : Short',
     'Dress length : Long',
     'Dress length : Court Train',
     'Sleek one shoulder design with flouncing trim makes it a style stand out.',
     'Waist:Dropped ',
     '(3958) Washable Pencil Peplum Dress Fully Lined Red',
     'Formal Bolero Embroidery Sequined Mother of The Bride Dress   Full Lined with Bone  Inner Pad: Yes   Dry Clean Only',
     ' Hit the scene in style with this chic mini dress!',
     'Modeng Womens College Wind Three-Dimensional Cut Dress',
     'Offers medium-weight stretch and hidden back zipper.',
     'SOFT STRETCHY JERSEY DRESS IN A THICK QUALITY MATERIAL',
     'Please see additional pictures for color pattern (Beige) and other beautiful details (all original tags and certificate of authenticity are included).',
     'Special applique design of good quality dress can make you become the focus.',
     'The dress is accented with oversized bow',
     'The princeton dress has a hidden back zip closure and measures 35 inch in length',
     'US Fairytailes Party Dress New Designer Long Gown Sizes 4-14 #2635',
     'Vertical, linear rows of different sized sequins, in light and dark gunmetal colors arranged to create ombre effect',
     'We cant help but fall in love with this beautifully breezy maxi dress.',
     'You can use this Dress for Office or Night Club, Cocktail, Formal, Spring, Autumn, Winter Party Dresses  This is our size chart for your reference:  1.',
     'Artful baroque embroidery lends a luxe quality to this flattering gown',
     'Dress color reference to picture red color only.',
     'Get a look that you will love with our beautiful acid wash dress!',
     ' Hand-made and Gorgeous design and high quality crystalsmakes the dress appropriate for a homecoming, a cocktail evening party, or other occasions.',
     'Model Info: Wearing Size 14, Height - 510", Shape - Hourglass']



# Fix the errors

from data_preprocessor import SentenceRemover
excluded_fname = 'data_manager/preprocess/excluded_phrases.pkl'
included_fname = 'data_manager/preprocess/included_phrases.pkl'

d = SentenceRemover(excluded_fname, included_fname)

# Rectify included
print "size of e: ", len(e)
for sent in e:
    print sent
    new_sent = d.mk_sent_comparable(sent)
    print new_sent
    print new_sent in d.included_sentences
    d.rectify_included(sent)
d.commit()

# Rectify excluded
print "size of i: ", len(i)
for sent in i:
    print sent
    new_sent = d.mk_sent_comparable(sent)
    print new_sent
    print new_sent in d.excluded_sentences
    d.rectify_excluded(sent)
d.commit()



# NOT excluded somehow.  This is a problem with ascii cause there was a bullet or something.
# For the most accurate measurements, please use our size chart .Our handling time is 3-5 days and shipment from China to US normally takes 7-15 days.
#
# Please check out other listing for bebe, french connection,  Guess Marciano sundress, Herve leger bandage dresses from celebritystyle
#
