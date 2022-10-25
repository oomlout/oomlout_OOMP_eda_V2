
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Protection"
    oIndex = "TPD2EUSB30"
    hexID = "SZKPOWERPROTECTIONTPD2EU3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPD2EUSB30', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:Texas_DRT-3', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tpd2eusb30a.pdf', 'kicadSymbolki_keywords': 'ESD protection USB 3.0', 'kicadSymbolki_description': '2-Channel ESD Protection for Super-Speed USB 3.0 Interface, DRT-3', 'kicadSymbolki_fp_filters': 'Texas*DRT*'}])
    newPart['name'].append('Power_Protection : TPD2EUSB30')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

