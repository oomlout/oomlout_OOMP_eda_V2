
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Touch"
    oIndex = "MPR121QR2"
    hexID = "SZKSENTOUCHMPR121QR2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MPR121QR2', 'kicadSymbolFootprint': 'Package_DFN_QFN:UQFN-20_3x3mm_P0.4mm', 'kicadSymbolDatasheet': 'https://resurgentsemi.com/wp-content/uploads/2018/09/MPR121_rev5-Resurgent.pdf?d453f8&d453f8', 'kicadSymbolki_keywords': 'Touch Sensor 12ch', 'kicadSymbolki_description': '12ch Touch Sensor controller, UQFN-20', 'kicadSymbolki_fp_filters': 'UQFN*3x3mm*P0.4mm*'}])
    newPart['name'].append('Sensor_Touch : MPR121QR2')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

