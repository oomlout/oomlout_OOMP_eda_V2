
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "DMN32D2LDF"
    hexID = "SZKTRANSISTORFETDMN32D2LDF"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'DMN32D2LDF', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-353_SC-70-5', 'kicadSymbolDatasheet': 'https://www.diodes.com/assets/Datasheets/ds31238.pdf', 'kicadSymbolki_keywords': 'N-FET', 'kicadSymbolki_description': 'Common Source Dual 400mA Id, 30V Vds, N-Channel MOSFET, 1.5Ohm Ron, SOT-353', 'kicadSymbolki_fp_filters': 'SOT?353*'}])
    newPart['name'].append('DMN32D2LDF')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

