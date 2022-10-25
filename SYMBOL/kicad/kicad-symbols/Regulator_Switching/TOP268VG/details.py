
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "TOP268VG"
    hexID = "SZKREGULATORSWITCHINGTOP268VG"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TOP264VG', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TOP268VG', 'kicadSymbolFootprint': 'Package_DIP:PowerIntegrations_eDIP-12B', 'kicadSymbolDatasheet': 'https://ac-dc.power.com/sites/default/files/product-docs/topswitch-jx_family_datasheet.pdf', 'kicadSymbolki_keywords': 'Integrated Off-Line Switcher with EcoSmart™ Technology', 'kicadSymbolki_description': 'TOPSwitch-JX Family, 112W Output Power, eDIP-12B', 'kicadSymbolki_fp_filters': 'PowerIntegrations?eDIP?12*'}])
    newPart['name'].append('Regulator_Switching : TOP268VG')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

