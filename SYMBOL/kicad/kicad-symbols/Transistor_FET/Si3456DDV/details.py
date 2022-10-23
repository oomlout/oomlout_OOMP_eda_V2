
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "Si3456DDV"
    hexID = "SZKTRANSISTORFETSI3456DDV"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'Si3456DDV', 'kicadSymbolFootprint': 'Package_SO:TSOP-6_1.65x3.05mm_P0.95mm', 'kicadSymbolDatasheet': 'https://www.vishay.com/docs/69075/si3456ddv.pdf', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '30V Vds, 6.3A Id, N-Channel MOSFET, TSOP-6', 'kicadSymbolki_fp_filters': 'TSOP*1.65x3.05mm*P0.95mm*'}])
    newPart['name'].append('Si3456DDV')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

