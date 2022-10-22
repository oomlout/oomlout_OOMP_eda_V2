
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "Thermistor_NTC_3Wire"
    hexID = "SZKDEVICETHERMISTORNTC3WIRE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'TH', 'kicadSymbolValue': 'Thermistor_NTC_3Wire', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'thermistor NTC resistor sensor RTD', 'kicadSymbolki_description': 'Temperature dependent resistor, negative temperature coefficient, 3-wire interface', 'kicadSymbolki_fp_filters': '*NTC* *Thermistor* PIN?ARRAY* bornier* *Terminal?Block*'}])
    newPart['name'].append('Thermistor_NTC_3Wire')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

