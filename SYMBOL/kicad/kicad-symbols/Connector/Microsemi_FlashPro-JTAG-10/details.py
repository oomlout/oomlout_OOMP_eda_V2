
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "Microsemi_FlashPro-JTAG-10"
    hexID = "SZKCNMSEMIFLASHPROJTAG1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'Microsemi_FlashPro-JTAG-10', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.microsemi.com/document-portal/doc_view/129973-lpf-ac386-an', 'kicadSymbolki_keywords': 'JTAG IDC10 Male Connector', 'kicadSymbolki_description': 'ACTEL FLASH PRO 3/4, JTAG, IDC10 Male Connector', 'kicadSymbolki_fp_filters': 'IDC?Header*2x05* Pin?Header*2x05*'}])
    newPart['name'].append('Microsemi_FlashPro-JTAG-10')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

