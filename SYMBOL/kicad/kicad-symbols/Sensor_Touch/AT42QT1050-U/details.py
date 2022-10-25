
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Touch"
    oIndex = "AT42QT1050-U"
    hexID = "SZKSENTOUCHAT42QT15U"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AT42QT1050-U', 'kicadSymbolFootprint': 'Package_CSP:WLCSP-12_1.403x1.555mm_P0.4mm_Stagger', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-9707-AT42-QTouch-BSW-AT42QT1050_Datasheet.pdf', 'kicadSymbolki_keywords': 'Touch QTouch Sensor Key', 'kicadSymbolki_description': 'Five-Key Touch Sensor, WLCSP-12', 'kicadSymbolki_fp_filters': 'WLCSP*1.403x1.555mm*P0.4mm*'}])
    newPart['name'].append('Sensor_Touch : AT42QT1050-U')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

