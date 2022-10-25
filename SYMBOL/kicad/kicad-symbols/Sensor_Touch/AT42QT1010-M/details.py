
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Touch"
    oIndex = "AT42QT1010-M"
    hexID = "SZKSENTOUCHAT42QT11M"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AT42QT1010-M', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-8-1EP_2x2mm_P0.5mm_EP0.9x1.5mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/40001946A.pdf', 'kicadSymbolki_keywords': 'Touch QTouch Sensor Key', 'kicadSymbolki_description': 'Single-key Touch Sensor, UDFN-8', 'kicadSymbolki_fp_filters': 'DFN*1EP*2x2mm*P0.5mm*'}])
    newPart['name'].append('Sensor_Touch : AT42QT1010-M')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

