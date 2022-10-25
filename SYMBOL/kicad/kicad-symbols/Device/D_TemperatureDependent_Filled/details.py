
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "D_TemperatureDependent_Filled"
    hexID = "SZKDEVICEDTEMPERATUREDEPENDENTFILL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'D_TemperatureDependent_Filled', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'temperature sensor diode', 'kicadSymbolki_description': 'Temperature dependent diode, filled shape', 'kicadSymbolki_fp_filters': 'TO-???* *_Diode_* *SingleDiode* D_*'}])
    newPart['name'].append('Device : D_TemperatureDependent_Filled')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

