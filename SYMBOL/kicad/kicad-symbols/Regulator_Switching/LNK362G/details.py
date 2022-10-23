
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LNK362G"
    hexID = "SZKREGULATORSWITCHINGLNK362G"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LNK362G', 'kicadSymbolFootprint': 'Package_DIP:PowerIntegrations_SMD-8B', 'kicadSymbolDatasheet': 'http://www.powerint.com/sites/default/files/product-docs/lnk362-364.pdf', 'kicadSymbolki_keywords': 'Energy Effi cient, Low Power Off-Line Switcher IC', 'kicadSymbolki_description': 'LinkSwitch-XT Family, 2.6W Output Power, SMD-8B', 'kicadSymbolki_fp_filters': 'PowerIntegrations?SMD?8B*'}])
    newPart['name'].append('LNK362G')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

