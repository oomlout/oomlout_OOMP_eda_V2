
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Protection"
    oIndex = "TPD4EUSB30"
    hexID = "SZKPOWERPROTECTIONTPD4EU3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPD4EUSB30', 'kicadSymbolFootprint': 'Package_SON:USON-10_2.5x1.0mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tpd2eusb30a.pdf', 'kicadSymbolki_keywords': 'ESD protection USB 3.0', 'kicadSymbolki_description': '4-Channel ESD Protection for Super-Speed USB 3.0 Interface, USON-10', 'kicadSymbolki_fp_filters': 'USON*2.5x1.0mm*P0.5mm*'}])
    newPart['name'].append('Power_Protection : TPD4EUSB30')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

