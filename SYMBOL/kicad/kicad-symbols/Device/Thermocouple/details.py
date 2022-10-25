
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "Thermocouple"
    hexID = "SZKDEVICETHERMOCOUPLE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'TC', 'kicadSymbolValue': 'Thermocouple', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'thermocouple temperature sensor cold junction', 'kicadSymbolki_description': 'Thermocouple', 'kicadSymbolki_fp_filters': 'PIN?ARRAY* bornier* *Terminal?Block* Thermo*Couple*'}])
    newPart['name'].append('Device : Thermocouple')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

