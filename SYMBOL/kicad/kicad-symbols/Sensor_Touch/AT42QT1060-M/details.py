
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Touch"
    oIndex = "AT42QT1060-M"
    hexID = "SZKSENTOUCHAT42QT16M"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AT42QT1060-M', 'kicadSymbolFootprint': 'Package_DFN_QFN:VQFN-28-1EP_4x4mm_P0.45mm_EP2.4x2.4mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-9505-AT42-QTouch-BSW-AT42QT1060_Datasheet.pdf', 'kicadSymbolki_keywords': 'Touch QTouch Sensor Key', 'kicadSymbolki_description': 'Six-Key Touch Sensor IC, VQFN-28', 'kicadSymbolki_fp_filters': 'VQFN*1EP*4x4mm*P0.45mm*'}])
    newPart['name'].append('Sensor_Touch : AT42QT1060-M')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

