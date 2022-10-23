
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "NPC45560-L"
    hexID = "SZKPOWERMANAGEMENTNPC4556L"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'NPC45560-H', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NPC45560-L', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-12-1EP_3x3mm_P0.5mm_EP2.05x2.86mm', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub/Collateral/NCP45560-D.PDF', 'kicadSymbolki_keywords': 'load switch', 'kicadSymbolki_description': 'Controlled load switch with low Ron, DFN-12', 'kicadSymbolki_fp_filters': '*DFN*12*'}])
    newPart['name'].append('NPC45560-L')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

