
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "MIC29752WT"
    hexID = "SZKREGULATORLINEARMIC29752WT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MIC29752WT', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-247-5_Vertical', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/devicedoc/20005685a.pdf', 'kicadSymbolki_keywords': '7.5A LDO linear voltage regulator adjustable positive', 'kicadSymbolki_description': '7.5A low dropout linear regulator, adjustable output, TO-247', 'kicadSymbolki_fp_filters': 'TO*247*'}])
    newPart['name'].append('Regulator_Linear : MIC29752WT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

