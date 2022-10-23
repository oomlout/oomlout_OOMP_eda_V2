
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LNK460K"
    hexID = "SZKREGULATORSWITCHINGLNK46K"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LNK457K', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LNK460K', 'kicadSymbolFootprint': 'Package_SO:PowerIntegrations_eSOP-12B', 'kicadSymbolDatasheet': 'http://www.powerint.com/sites/default/files/product-docs/linkswitch-pl_family_datasheet.pdf', 'kicadSymbolki_keywords': 'LED Driver IC with TRIAC Dimming, Single-Stage PFC and Constant Current Control for Non-Isolated Applications', 'kicadSymbolki_description': 'LinkSwitch-PL Family, 16W Output Power, eSOP-12B', 'kicadSymbolki_fp_filters': 'PowerIntegrations?eSOP?12B*'}])
    newPart['name'].append('LNK460K')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

