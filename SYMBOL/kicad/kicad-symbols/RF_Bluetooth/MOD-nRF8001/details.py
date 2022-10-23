
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Bluetooth"
    oIndex = "MOD-nRF8001"
    hexID = "SZKRFBLUETOOTHMODNRF81"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MOD-nRF8001', 'kicadSymbolFootprint': 'RF_Module:MOD-nRF8001', 'kicadSymbolDatasheet': 'https://www.olimex.com/Products/Modules/RF/MOD-nRF8001/', 'kicadSymbolki_keywords': 'Bluetooth Low Energy nRF8001', 'kicadSymbolki_description': 'Bluetooth Low Energy module based on nRF8001 chipset', 'kicadSymbolki_fp_filters': 'MOD?nRF8001*'}])
    newPart['name'].append('MOD-nRF8001')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

