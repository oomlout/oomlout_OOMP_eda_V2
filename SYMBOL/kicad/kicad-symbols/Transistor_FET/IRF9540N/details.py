
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRF9540N"
    hexID = "SZKTRANSISTORFETIRF954N"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRF9540N', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-3_Vertical', 'kicadSymbolDatasheet': 'http://www.irf.com/product-info/datasheets/data/irf9540n.pdf', 'kicadSymbolki_keywords': 'P-Channel MOSFET HEXFET', 'kicadSymbolki_description': '-23A Id, -100V Vds, 117mOhm Rds, P-Channel HEXFET Power MOSFET, TO-220', 'kicadSymbolki_fp_filters': 'TO?220*'}])
    newPart['name'].append('IRF9540N')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

