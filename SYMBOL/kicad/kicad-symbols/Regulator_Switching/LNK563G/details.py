
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LNK563G"
    hexID = "SZKREGULATORSWITCHINGLNK563G"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LNK562G', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LNK563G', 'kicadSymbolFootprint': 'Package_DIP:PowerIntegrations_SMD-8B', 'kicadSymbolDatasheet': 'http://www.powerint.com/sites/default/files/product-docs/linklp_family_datasheet.pdf', 'kicadSymbolki_keywords': 'Energy Efficient Off-Line Switcher IC for Linear Transformer Replacement', 'kicadSymbolki_description': 'LinkSwitch-LP Family, 2.5W Output Power, SMD-8B', 'kicadSymbolki_fp_filters': 'PowerIntegrations?SMD?8B*'}])
    newPart['name'].append('LNK563G')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

