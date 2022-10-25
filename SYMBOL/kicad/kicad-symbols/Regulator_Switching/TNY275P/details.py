
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "TNY275P"
    hexID = "SZKREGULATORSWITCHINGTNY275P"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TNY274P', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TNY275P', 'kicadSymbolFootprint': 'Package_DIP:PowerIntegrations_PDIP-8C', 'kicadSymbolDatasheet': 'http://www.powerint.com/sites/default/files/product-docs/tny274-280.pdf', 'kicadSymbolki_keywords': 'Energy-Efficient, Off-Line Switcher With Enhanced Flexibility and Extended Power Range', 'kicadSymbolki_description': 'TinySwitch-III Family, 11.5W Output Power, DIP-8C', 'kicadSymbolki_fp_filters': 'PowerIntegrations?PDIP?8C*'}])
    newPart['name'].append('Regulator_Switching : TNY275P')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

