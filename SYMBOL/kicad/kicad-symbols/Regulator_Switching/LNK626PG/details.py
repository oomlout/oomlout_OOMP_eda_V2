
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LNK626PG"
    hexID = "SZKREGULATORSWITCHINGLNK626PG"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LNK623PG', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LNK626PG', 'kicadSymbolFootprint': 'Package_DIP:PowerIntegrations_PDIP-8C', 'kicadSymbolDatasheet': 'http://www.powerint.com/sites/default/files/product-docs/linkcv_family_datasheet.pdf', 'kicadSymbolki_keywords': 'Energy-Efficient, Off-line Switcher with Accurate Primary-side Constant-Voltage Control', 'kicadSymbolki_description': 'LinkSwitch-CV Family, 10W Output Power, DIP-8C', 'kicadSymbolki_fp_filters': 'PowerIntegrations?PDIP?8C*'}])
    newPart['name'].append('Regulator_Switching : LNK626PG')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

