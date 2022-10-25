
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Buffer"
    oIndex = "LM6321H"
    hexID = "SZKAMPLIFIERBUFFERLM6321H"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM6321H', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-5-8', 'kicadSymbolDatasheet': 'http://www.electronica60norte.com/mwfls/pdf/LM6221.pdf', 'kicadSymbolki_keywords': 'single buffer', 'kicadSymbolki_description': 'High Speed Buffer, TO-5-8', 'kicadSymbolki_fp_filters': 'TO?5*'}])
    newPart['name'].append('Amplifier_Buffer : LM6321H')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

