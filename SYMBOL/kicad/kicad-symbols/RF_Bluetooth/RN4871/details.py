
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Bluetooth"
    oIndex = "RN4871"
    hexID = "SZKRFBLUETOOTHRN4871"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'RN4871', 'kicadSymbolFootprint': 'RF_Module:Microchip_RN4871', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/50002489A.pdf', 'kicadSymbolki_keywords': 'Bluetooth Low Energy 4.2 Module', 'kicadSymbolki_description': 'Bluetooth Low Energy 4.2 Module', 'kicadSymbolki_fp_filters': 'RF*Module:Microchip*RN4871*'}])
    newPart['name'].append('RN4871')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

