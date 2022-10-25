
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LNK363P"
    hexID = "SZKREGULATORSWITCHINGLNK363P"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LNK362P', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LNK363P', 'kicadSymbolFootprint': 'Package_DIP:PowerIntegrations_PDIP-8B', 'kicadSymbolDatasheet': 'http://www.powerint.com/sites/default/files/product-docs/lnk362-364.pdf', 'kicadSymbolki_keywords': 'Energy Effi cient, Low Power Off-Line Switcher IC', 'kicadSymbolki_description': 'LinkSwitch-XT Family, 4.7W Output Power, DIP-8B', 'kicadSymbolki_fp_filters': 'PowerIntegrations?PDIP?8B*'}])
    newPart['name'].append('Regulator_Switching : LNK363P')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

