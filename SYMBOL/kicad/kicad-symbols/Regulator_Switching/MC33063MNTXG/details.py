
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "MC33063MNTXG"
    hexID = "SZKREGULATORSWITCHINGMC3363MNTXG"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MC33063MNTXG', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-8-1EP_4x4mm_P0.8mm_EP2.5x3.6mm', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub_link/Collateral/MC34063A-D.PDF', 'kicadSymbolki_keywords': 'smps buck boost inverting', 'kicadSymbolki_description': '1.5A, step-up/down/inverting switching regulator, 3-40V Vin, 100kHz, DFN-8', 'kicadSymbolki_fp_filters': 'DFN*EP*4x4mm*P0.8mm*'}])
    newPart['name'].append('MC33063MNTXG')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

