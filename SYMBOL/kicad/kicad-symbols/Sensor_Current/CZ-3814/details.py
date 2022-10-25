
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Current"
    oIndex = "CZ-3814"
    hexID = "SZKSENCURRENTCZ3814"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'CZ-3813', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CZ-3814', 'kicadSymbolFootprint': 'Sensor_Current:AKM_CZ_SSOP-10_6.5x8.1mm_P0.95mm', 'kicadSymbolDatasheet': 'http://www.akm.com/akm/en/file/datasheet/CZ-3814.pdf', 'kicadSymbolki_keywords': 'hall effect current sensor', 'kicadSymbolki_description': 'Coreless Current Sensor, Bidirectional, -50.0A to +50.0A, 40mV/A, VSOP-24', 'kicadSymbolki_fp_filters': 'AKM*CZ*SSOP*6.5x8.1mm*P0.95mm*'}])
    newPart['name'].append('Sensor_Current : CZ-3814')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

