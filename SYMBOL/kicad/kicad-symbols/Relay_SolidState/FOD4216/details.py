
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay_SolidState"
    oIndex = "FOD4216"
    hexID = "SZKRELAYSOLIDSTATEFOD4216"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'FOD420', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'FOD4216', 'kicadSymbolFootprint': 'Package_DIP:DIP-6_W7.62mm', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/FOD4218-D.PDF', 'kicadSymbolki_keywords': 'Opto-Triac Opto Triac Random Phase', 'kicadSymbolki_description': 'Random Phase Opto-Triac, Vdrm 600V, Ift 0.75mA, Itm 300mA, DIP6', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Relay_SolidState : FOD4216')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

