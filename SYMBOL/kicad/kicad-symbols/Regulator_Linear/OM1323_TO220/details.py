
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "OM1323_TO220"
    hexID = "SZKREGULATORLINEAROM1323TO22"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM337_TO220', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'OM1323_TO220', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-3_Vertical', 'kicadSymbolDatasheet': 'http://www.irf.com/product-info/datasheets/hirel/om1323.pdf', 'kicadSymbolki_keywords': 'Adjustable Voltage Regulator 1.5A Negative', 'kicadSymbolki_description': 'Negative 1.5A 35V Adjustable Linear Regulator, TO-220', 'kicadSymbolki_fp_filters': 'TO?220*'}])
    newPart['name'].append('OM1323_TO220')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

