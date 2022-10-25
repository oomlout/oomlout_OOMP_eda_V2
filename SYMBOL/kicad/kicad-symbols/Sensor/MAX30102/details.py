
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor"
    oIndex = "MAX30102"
    hexID = "SZKSENMAX312"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX30102', 'kicadSymbolFootprint': 'OptoDevice:Maxim_OLGA-14_3.3x5.6mm_P0.8mm', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX30102.pdf', 'kicadSymbolki_keywords': 'Heart Rate', 'kicadSymbolki_description': 'Heart Rate Sensor, 14-OLGA', 'kicadSymbolki_fp_filters': 'Maxim*OLGA*3.3x5.6mm*P0.8mm*'}])
    newPart['name'].append('Sensor : MAX30102')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

