
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LNK603DG"
    hexID = "SZKREGULATORSWITCHINGLNK63DG"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LNK603DG', 'kicadSymbolFootprint': 'Package_SO:PowerIntegrations_SO-8C', 'kicadSymbolDatasheet': 'http://www.powerint.com/sites/default/files/product-docs/linkswitch-ii_family_datasheet.pdf', 'kicadSymbolki_keywords': 'Energy-Efficient, Accurate CV/CC Switcher for Adapters and Chargers', 'kicadSymbolki_description': 'LinkSwitch-II Family, 3.3W Output Power, SO-8C', 'kicadSymbolki_fp_filters': 'PowerIntegrations?SO?8C*'}])
    newPart['name'].append('Regulator_Switching : LNK603DG')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

