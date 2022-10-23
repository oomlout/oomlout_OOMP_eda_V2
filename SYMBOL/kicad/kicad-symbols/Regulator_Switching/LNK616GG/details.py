
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LNK616GG"
    hexID = "SZKREGULATORSWITCHINGLNK616GG"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LNK606GG', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LNK616GG', 'kicadSymbolFootprint': 'Package_DIP:PowerIntegrations_SMD-8C', 'kicadSymbolDatasheet': 'http://www.powerint.com/sites/default/files/product-docs/linkswitch-ii_family_datasheet.pdf', 'kicadSymbolki_keywords': 'Energy-Efficient, Accurate CV/CC Switcher for Adapters and Chargers', 'kicadSymbolki_description': 'LinkSwitch-II Family, 6.1W Output Power, SMD-8C', 'kicadSymbolki_fp_filters': 'PowerIntegrations?SMD?8C*'}])
    newPart['name'].append('LNK616GG')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

