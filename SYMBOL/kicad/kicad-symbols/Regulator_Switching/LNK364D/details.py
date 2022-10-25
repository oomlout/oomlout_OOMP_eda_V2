
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LNK364D"
    hexID = "SZKREGULATORSWITCHINGLNK364D"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LNK362D', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LNK364D', 'kicadSymbolFootprint': 'Package_SO:PowerIntegrations_SO-8C', 'kicadSymbolDatasheet': 'http://www.powerint.com/sites/default/files/product-docs/lnk362-364.pdf', 'kicadSymbolki_keywords': 'Energy Effi cient, Low Power Off-Line Switcher IC', 'kicadSymbolki_description': 'LinkSwitch-XT Family, 6W Output Power, SO-8C', 'kicadSymbolki_fp_filters': 'PowerIntegrations?SO?8C*'}])
    newPart['name'].append('Regulator_Switching : LNK364D')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

