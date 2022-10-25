
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "TOP258YN"
    hexID = "SZKREGULATORSWITCHINGTOP258YN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TOP254YN', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TOP258YN', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:PowerIntegrations_TO-220-7C', 'kicadSymbolDatasheet': 'https://ac-dc.power.com/sites/default/files/product-docs/topswitch-hx_family_datasheet.pdf', 'kicadSymbolki_keywords': 'Eco Smart Off-Line Switcher, Extendend Power Range', 'kicadSymbolki_description': 'TOPSwitch-HX Family, 148W Output Power', 'kicadSymbolki_fp_filters': 'PowerIntegrations*TO?220?7C*'}])
    newPart['name'].append('Regulator_Switching : TOP258YN')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

