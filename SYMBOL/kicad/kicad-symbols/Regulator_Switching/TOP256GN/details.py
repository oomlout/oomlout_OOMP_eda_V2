
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "TOP256GN"
    hexID = "SZKREGULATORSWITCHINGTOP256GN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TOP252GN', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TOP256GN', 'kicadSymbolFootprint': 'Package_DIP:PowerIntegrations_SMD-8C', 'kicadSymbolDatasheet': 'https://ac-dc.power.com/sites/default/files/product-docs/topswitch-hx_family_datasheet.pdf', 'kicadSymbolki_keywords': 'Eco Smart Off-Line Switcher, Extendend Power Range', 'kicadSymbolki_description': 'TOPSwitch-HX Family, 26W Output Power', 'kicadSymbolki_fp_filters': 'PowerIntegrations?SMD?8C*'}])
    newPart['name'].append('Regulator_Switching : TOP256GN')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

