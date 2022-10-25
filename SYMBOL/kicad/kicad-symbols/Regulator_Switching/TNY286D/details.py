
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "TNY286D"
    hexID = "SZKREGULATORSWITCHINGTNY286D"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TNY284D', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TNY286D', 'kicadSymbolFootprint': 'Package_SO:PowerIntegrations_SO-8C', 'kicadSymbolDatasheet': 'https://ac-dc.power.com/sites/default/files/product-docs/tinyswitch-4_family_datasheet.pdf', 'kicadSymbolki_keywords': 'Energy-Efficient, Off-Line Switcher With Line Compensated Overload Power', 'kicadSymbolki_description': 'TinySwitch-4 Family, 15W Output Power, SO-8C', 'kicadSymbolki_fp_filters': 'PowerIntegrations?SO?8C*'}])
    newPart['name'].append('Regulator_Switching : TNY286D')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

