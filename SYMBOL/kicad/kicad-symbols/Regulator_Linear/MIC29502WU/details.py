
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "MIC29502WU"
    hexID = "SZKREGULATORLINEARMIC2952WU"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MIC29302WU', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MIC29502WU', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-263-5_TabPin3', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/devicedoc/20005685a.pdf', 'kicadSymbolki_keywords': '5A LDO linear voltage regulator adjustable positive', 'kicadSymbolki_description': '5A low dropout linear regulator, adjustable output, TO-263', 'kicadSymbolki_fp_filters': 'TO*263*'}])
    newPart['name'].append('Regulator_Linear : MIC29502WU')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

