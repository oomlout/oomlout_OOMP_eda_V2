
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "SC4503TSK"
    hexID = "SZKREGULATORSWITCHINGSC453TSK"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SC4503TSK', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TSOT-23-5', 'kicadSymbolDatasheet': 'https://www.semtech.com/uploads/documents/sc4503.pdf', 'kicadSymbolki_keywords': '1.9A 1.3MHz Step-Up DC/DC', 'kicadSymbolki_description': '1.9A, 1.3MHz Step-Up DC/DC Converter, 2.5V-20V output voltage, TSOT23', 'kicadSymbolki_fp_filters': 'TSOT*23*'}])
    newPart['name'].append('SC4503TSK')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

