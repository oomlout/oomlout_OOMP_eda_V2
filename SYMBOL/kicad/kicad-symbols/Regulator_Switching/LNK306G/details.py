
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LNK306G"
    hexID = "SZKREGULATORSWITCHINGLNK36G"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LNK302G', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LNK306G', 'kicadSymbolFootprint': 'Package_DIP:PowerIntegrations_SMD-8B', 'kicadSymbolDatasheet': 'http://www.powerint.com/sites/default/files/product-docs/lnk302_304-306.pdf', 'kicadSymbolki_keywords': 'Lowest Component Count, Energy-Efficient Off-Line Switcher IC', 'kicadSymbolki_description': 'LinkSwitch-TN Family, 360mA Output Current, SMD-8B', 'kicadSymbolki_fp_filters': 'PowerIntegrations?SMD?8B*'}])
    newPart['name'].append('Regulator_Switching : LNK306G')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

