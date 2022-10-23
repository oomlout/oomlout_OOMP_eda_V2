
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "EMH3"
    hexID = "SZKTRANSISTORBJTEMH3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'EMH3', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-563', 'kicadSymbolDatasheet': 'http://rohmfs.rohm.com/en/products/databook/datasheet/discrete/transistor/digital/emh3t2r-e.pdf', 'kicadSymbolki_keywords': 'Dual NPN Transistor', 'kicadSymbolki_description': '0.1A Ic, 50V Vce, Dual NPN Input Resistor Transistors, SOT-563', 'kicadSymbolki_fp_filters': 'SOT?563*'}])
    newPart['name'].append('EMH3')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

