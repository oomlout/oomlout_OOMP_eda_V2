
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LNK562P"
    hexID = "SZKREGULATORSWITCHINGLNK562P"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LNK562P', 'kicadSymbolFootprint': 'Package_DIP:PowerIntegrations_PDIP-8B', 'kicadSymbolDatasheet': 'http://www.powerint.com/sites/default/files/product-docs/linklp_family_datasheet.pdf', 'kicadSymbolki_keywords': 'Energy Efficient Off-Line Switcher IC for Linear Transformer Replacement', 'kicadSymbolki_description': 'LinkSwitch-LP Family, 1.9W Output Power, DIP-8B', 'kicadSymbolki_fp_filters': 'PowerIntegrations?PDIP?8B*'}])
    newPart['name'].append('Regulator_Switching : LNK562P')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

