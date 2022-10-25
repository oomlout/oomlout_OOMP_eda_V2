
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "Thermistor_US"
    hexID = "SZKDEVICETHERMISTORUS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'TH', 'kicadSymbolValue': 'Thermistor_US', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'R res thermistor', 'kicadSymbolki_description': 'Thermistor, temperature dependent resistor, US symbol', 'kicadSymbolki_fp_filters': 'R_*'}])
    newPart['name'].append('Device : Thermistor_US')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

