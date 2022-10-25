
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Module"
    oIndex = "Omega2+"
    hexID = "SZKMCUMOOMEGA2+"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'Omega2+', 'kicadSymbolFootprint': 'Module:Onion_Omega2+', 'kicadSymbolDatasheet': 'https://docs.onion.io/omega2-docs/omega2p.html', 'kicadSymbolki_keywords': 'onion omega module', 'kicadSymbolki_description': 'Iot Computer Module by Onion', 'kicadSymbolki_fp_filters': 'Onion*Omega2+*'}])
    newPart['name'].append('MCU_Module : Omega2+')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

