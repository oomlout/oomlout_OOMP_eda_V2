
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "Thermistor_PTC_US"
    hexID = "SZKDEVICETHERMISTORPTCUS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'TH', 'kicadSymbolValue': 'Thermistor_PTC_US', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'resistor PTC thermistor sensor RTD', 'kicadSymbolki_description': 'Temperature dependent resistor, positive temperature coefficient, US symbol', 'kicadSymbolki_fp_filters': '*PTC* *Thermistor* PIN?ARRAY* bornier* *Terminal?Block* R_*'}])
    newPart['name'].append('Device : Thermistor_PTC_US')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

