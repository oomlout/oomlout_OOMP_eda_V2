
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "R_Pack04_SIP_Split"
    hexID = "SZKDEVICERPACK4SIPSPLIT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'RN', 'kicadSymbolValue': 'R_Pack04_SIP_Split', 'kicadSymbolFootprint': 'Resistor_THT:R_Array_SIP8', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/31509/csc.pdf', 'kicadSymbolki_keywords': 'R network parallel topology isolated', 'kicadSymbolki_description': '4 resistor network, parallel topology, SIP package, split', 'kicadSymbolki_fp_filters': 'R?Array?SIP*'}])
    newPart['name'].append('Device : R_Pack04_SIP_Split')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

