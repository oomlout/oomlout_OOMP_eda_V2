
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Temperature"
    oIndex = "KT100"
    hexID = "SZKSENTEMPERATUREKT1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'KTY81', 'kicadSymbolReference': 'TH', 'kicadSymbolValue': 'KT100', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.b-kainka.de/Daten/Sensor/kty10.pdf', 'kicadSymbolki_keywords': 'silicon temperature sensors', 'kicadSymbolki_description': 'KTY10/KT100 series silicon temperature sensors', 'kicadSymbolki_fp_filters': 'SOD?70*'}])
    newPart['name'].append('Sensor_Temperature : KT100')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

