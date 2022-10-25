
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Bluetooth"
    oIndex = "RN42"
    hexID = "SZKRFBLUETOOTHRN42"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'RN42', 'kicadSymbolFootprint': 'RF_Module:RN42', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/rn-42-ds-v2.32r.pdf', 'kicadSymbolki_keywords': 'Bluetooth Module', 'kicadSymbolki_description': 'Class 2 Bluetooth Module with on-board antenna', 'kicadSymbolki_fp_filters': 'RN42*'}])
    newPart['name'].append('RF_Bluetooth : RN42')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

