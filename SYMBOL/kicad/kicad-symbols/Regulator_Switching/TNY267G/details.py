
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "TNY267G"
    hexID = "SZKREGULATORSWITCHINGTNY267G"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TNY263G', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TNY267G', 'kicadSymbolFootprint': 'Package_DIP:PowerIntegrations_SMD-8B', 'kicadSymbolDatasheet': 'http://www.powerint.com/sites/default/files/product-docs/tny263_268.pdf', 'kicadSymbolki_keywords': 'Enhanced, Energy Efficient, Low Power Off-line Switcher', 'kicadSymbolki_description': 'TinySwitch-II Family, 12W Output Power, SMD-8B', 'kicadSymbolki_fp_filters': 'PowerIntegrations?SMD?8B*'}])
    newPart['name'].append('TNY267G')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

