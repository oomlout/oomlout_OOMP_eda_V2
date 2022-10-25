
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "Thermistor_PTC_3Wire"
    hexID = "SZKDEVICETHERMISTORPTC3WIRE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'TH', 'kicadSymbolValue': 'Thermistor_PTC_3Wire', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'resistor PTC thermistor sensor RTD', 'kicadSymbolki_description': 'Temperature dependent resistor, positive temperature coefficient, 3-wire interface', 'kicadSymbolki_fp_filters': 'PIN_ARRAY_3X1 bornier3 TerminalBlock*3pol'}])
    newPart['name'].append('Device : Thermistor_PTC_3Wire')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

