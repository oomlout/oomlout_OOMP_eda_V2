
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Bluetooth"
    oIndex = "RN42N"
    hexID = "SZKRFBLUETOOTHRN42N"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'RN42N', 'kicadSymbolFootprint': 'RF_Module:RN42N', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/rn-42-ds-v2.32r.pdf', 'kicadSymbolki_keywords': 'Bluetooth Module', 'kicadSymbolki_description': 'Class 2 Bluetooth Module without antenna', 'kicadSymbolki_fp_filters': 'RN42N*'}])
    newPart['name'].append('RN42N')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

