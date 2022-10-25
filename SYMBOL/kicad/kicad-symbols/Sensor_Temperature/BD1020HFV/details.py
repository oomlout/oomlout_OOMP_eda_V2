
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Temperature"
    oIndex = "BD1020HFV"
    hexID = "SZKSENTEMPERATUREBD12HFV"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BD1020HFV', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:HVSOF5', 'kicadSymbolDatasheet': 'http://rohmfs.rohm.com/en/products/databook/datasheet/ic/sensor/temperature/bd1020hfv-e.pdf', 'kicadSymbolki_keywords': 'Temperature sensor', 'kicadSymbolki_description': 'Analog Output Temperature Sensor', 'kicadSymbolki_fp_filters': 'HVSOF5*'}])
    newPart['name'].append('Sensor_Temperature : BD1020HFV')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

