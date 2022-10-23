
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "MAX5035BUPA"
    hexID = "SZKREGULATORSWITCHINGMAX535BUPA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MAX5035AUPA', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX5035BUPA', 'kicadSymbolFootprint': 'Package_DIP:DIP-8_W7.62mm', 'kicadSymbolDatasheet': 'http://datasheets.maximintegrated.com/en/ds/MAX5035.pdf', 'kicadSymbolki_keywords': '5V 1A Step-Down Converter 76V', 'kicadSymbolki_description': '1A, High-Efficiency Step-Down DC-DC Converter, 5V fixed output voltage, Vin 76V, PDIP-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('MAX5035BUPA')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

