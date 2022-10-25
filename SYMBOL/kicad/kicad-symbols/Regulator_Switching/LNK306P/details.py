
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LNK306P"
    hexID = "SZKREGULATORSWITCHINGLNK36P"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LNK302P', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LNK306P', 'kicadSymbolFootprint': 'Package_DIP:PowerIntegrations_PDIP-8B', 'kicadSymbolDatasheet': 'http://www.powerint.com/sites/default/files/product-docs/lnk302_304-306.pdf', 'kicadSymbolki_keywords': 'Lowest Component Count, Energy-Efficient Off-Line Switcher IC', 'kicadSymbolki_description': 'LinkSwitch-TN Family, 360mA Output Current, DIP-8B', 'kicadSymbolki_fp_filters': 'PowerIntegrations?PDIP?8B*'}])
    newPart['name'].append('Regulator_Switching : LNK306P')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

