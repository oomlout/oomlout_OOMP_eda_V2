
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Reference_Voltage"
    oIndex = "MAX6241"
    hexID = "SZKREFERENCEVOLTAGEMAX6241"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MAX6350', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX6241', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://datasheets.maximintegrated.com/en/ds/MAX6225-MAX6250.pdf', 'kicadSymbolki_keywords': 'precision voltage reference', 'kicadSymbolki_description': '1ppm/°C Low-Noise Precision +4.096V Voltage Reference, SO-8/DIP-8', 'kicadSymbolki_fp_filters': 'SOIC*P1.27mm* DIP*W7.62mm*'}])
    newPart['name'].append('MAX6241')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

