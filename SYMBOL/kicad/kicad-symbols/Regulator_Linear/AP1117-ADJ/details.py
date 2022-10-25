
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "AP1117-ADJ"
    hexID = "SZKREGULATORLINEARAP1117ADJ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AP1117-ADJ', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-223-3_TabPin2', 'kicadSymbolDatasheet': 'http://www.diodes.com/datasheets/AP1117.pdf', 'kicadSymbolki_keywords': 'linear regulator ldo adjustable positive obsolete', 'kicadSymbolki_description': '1A Low Dropout regulator, positive, adjustable output, SOT-223', 'kicadSymbolki_fp_filters': 'SOT?223*TabPin2*'}])
    newPart['name'].append('Regulator_Linear : AP1117-ADJ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

