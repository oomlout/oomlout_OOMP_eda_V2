
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "TOP265EG"
    hexID = "SZKREGULATORSWITCHINGTOP265EG"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TOP264EG', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TOP265EG', 'kicadSymbolFootprint': 'Package_SIP:PowerIntegrations_eSIP-7C', 'kicadSymbolDatasheet': 'https://ac-dc.power.com/sites/default/files/product-docs/topswitch-jx_family_datasheet.pdf', 'kicadSymbolki_keywords': 'Integrated Off-Line Switcher with EcoSmart™ Technology', 'kicadSymbolki_description': 'TOPSwitch-JX Family, 57W Output Power, eSIP-7C', 'kicadSymbolki_fp_filters': 'PowerIntegrations?eSIP?7C*'}])
    newPart['name'].append('Regulator_Switching : TOP265EG')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

