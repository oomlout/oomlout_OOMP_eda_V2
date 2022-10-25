
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "TNY268P"
    hexID = "SZKREGULATORSWITCHINGTNY268P"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TNY263P', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TNY268P', 'kicadSymbolFootprint': 'Package_DIP:PowerIntegrations_PDIP-8B', 'kicadSymbolDatasheet': 'http://www.powerint.com/sites/default/files/product-docs/tny263_268.pdf', 'kicadSymbolki_keywords': 'Enhanced, Energy Efficient, Low Power Off-line Switcher', 'kicadSymbolki_description': 'TinySwitch-II Family, 15W Output Power, DIP-8B', 'kicadSymbolki_fp_filters': 'PowerIntegrations?PDIP?8B*'}])
    newPart['name'].append('Regulator_Switching : TNY268P')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

