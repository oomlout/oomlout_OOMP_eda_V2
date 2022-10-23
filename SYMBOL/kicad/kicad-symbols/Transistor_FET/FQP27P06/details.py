
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "FQP27P06"
    hexID = "SZKTRANSISTORFETFQP27P6"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IRF9540N', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'FQP27P06', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-3_Vertical', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/FQP27P06-D.PDF', 'kicadSymbolki_keywords': 'QFET P-Channel MOSFET', 'kicadSymbolki_description': '-27A Id, -60V Vds, QFET P-Channel MOSFET, TO-220', 'kicadSymbolki_fp_filters': 'TO?220*'}])
    newPart['name'].append('FQP27P06')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

