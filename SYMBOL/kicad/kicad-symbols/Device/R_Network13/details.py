
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "R_Network13"
    hexID = "SZKDEVICERNETWORK13"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'RN', 'kicadSymbolValue': 'R_Network13', 'kicadSymbolFootprint': 'Resistor_THT:R_Array_SIP14', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/31509/csc.pdf', 'kicadSymbolki_keywords': 'R network star-topology', 'kicadSymbolki_description': '13 resistor network, star topology, bussed resistors, small symbol', 'kicadSymbolki_fp_filters': 'R?Array?SIP*'}])
    newPart['name'].append('R_Network13')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

