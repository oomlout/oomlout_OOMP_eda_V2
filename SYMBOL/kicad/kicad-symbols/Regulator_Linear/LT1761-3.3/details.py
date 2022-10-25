
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LT1761-3.3"
    hexID = "SZKREGULATORLINEARLT176133"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LT1761-5', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT1761-3.3', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TSOT-23-5', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/1761sff.pdf', 'kicadSymbolki_keywords': 'REGULATOR POSITIVE POWER LDO', 'kicadSymbolki_description': 'MICROPOWER Low Noise 3.3V 100mA LDO regulator, TSOT-23-5', 'kicadSymbolki_fp_filters': 'TSOT?23*'}])
    newPart['name'].append('Regulator_Linear : LT1761-3.3')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

