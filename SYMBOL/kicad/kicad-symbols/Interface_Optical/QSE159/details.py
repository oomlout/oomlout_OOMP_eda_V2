
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_Optical"
    oIndex = "QSE159"
    hexID = "SZKINTERFACEOPTICALQSE159"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'QSE159', 'kicadSymbolFootprint': 'OptoDevice:ONSemi_QSE15x', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub/Collateral/QSE159-D.pdf', 'kicadSymbolki_keywords': 'opto IR', 'kicadSymbolki_description': 'Plastic Silicon Photosensor', 'kicadSymbolki_fp_filters': '*QSE15*'}])
    newPart['name'].append('QSE159')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

