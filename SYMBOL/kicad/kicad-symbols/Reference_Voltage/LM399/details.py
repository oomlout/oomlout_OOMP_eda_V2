
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Reference_Voltage"
    oIndex = "LM399"
    hexID = "SZKREFERENCEVOLTAGELM399"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM399', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:Analog_TO-46-4_ThermalShield', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/199399fc.pdf', 'kicadSymbolki_keywords': 'Zener diode device voltage reference', 'kicadSymbolki_description': 'Precision Reference, 6.95V, Buried Zener Diode with Thermal Shielding Can, TO-46-4', 'kicadSymbolki_fp_filters': 'Analog*TO?46*'}])
    newPart['name'].append('LM399')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

