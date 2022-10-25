
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LNK3202P"
    hexID = "SZKREGULATORSWITCHINGLNK322P"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LNK3202P', 'kicadSymbolFootprint': 'Package_DIP:PowerIntegrations_PDIP-8C', 'kicadSymbolDatasheet': 'https://ac-dc.power.com/sites/default/files/product-docs/LinkSwitch-TN2_family_datasheet.pdf', 'kicadSymbolki_keywords': 'Lowest Component Count, Energy-Efficient Off-Line Switcher IC', 'kicadSymbolki_description': 'LinkSwitch-TN2 Family, 80mA Output Current, DIP-8C', 'kicadSymbolki_fp_filters': 'PowerIntegrations?PDIP?8C*'}])
    newPart['name'].append('Regulator_Switching : LNK3202P')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

