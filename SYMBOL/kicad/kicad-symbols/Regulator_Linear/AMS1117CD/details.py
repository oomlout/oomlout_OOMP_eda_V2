
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "AMS1117CD"
    hexID = "SZKREGULATORLINEARAMS1117CD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AMS1117CD', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-252-3_TabPin2', 'kicadSymbolDatasheet': 'http://www.advanced-monolithic.com/pdf/ds1117.pdf', 'kicadSymbolki_keywords': 'linear regulator ldo fixed positive', 'kicadSymbolki_description': '1A Low Dropout regulator, positive, adjustable output, TO-252', 'kicadSymbolki_fp_filters': 'TO?252*TabPin2*'}])
    newPart['name'].append('Regulator_Linear : AMS1117CD')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

