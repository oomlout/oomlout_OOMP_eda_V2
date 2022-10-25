
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Touch"
    oIndex = "AT42QT1050-M"
    hexID = "SZKSENTOUCHAT42QT15M"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AT42QT1050-M', 'kicadSymbolFootprint': 'Package_DFN_QFN:VQFN-20-1EP_3x3mm_P0.45mm_EP1.55x1.55mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-9707-AT42-QTouch-BSW-AT42QT1050_Datasheet.pdf', 'kicadSymbolki_keywords': 'Touch QTouch Sensor Key', 'kicadSymbolki_description': 'Five-Key Touch Sensor, VQFN-20', 'kicadSymbolki_fp_filters': 'VQFN*1EP*3x3mm*P0.45mm*'}])
    newPart['name'].append('Sensor_Touch : AT42QT1050-M')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

