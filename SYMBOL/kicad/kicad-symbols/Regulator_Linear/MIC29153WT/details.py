
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "MIC29153WT"
    hexID = "SZKREGULATORLINEARMIC29153WT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MIC29153WT', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-5_P3.4x3.7mm_StaggerEven_Lead3.8mm_Vertical', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/devicedoc/20005685a.pdf', 'kicadSymbolki_keywords': '1.5A LDO linear voltage regulator adjustable positive', 'kicadSymbolki_description': '1.5A low dropout linear regulator, adjustable output, TO-220', 'kicadSymbolki_fp_filters': 'TO*220*'}])
    newPart['name'].append('Regulator_Linear : MIC29153WT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

