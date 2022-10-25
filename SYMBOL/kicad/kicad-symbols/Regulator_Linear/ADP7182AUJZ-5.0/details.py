
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "ADP7182AUJZ-5.0"
    hexID = "SZKREGULATORLINEARADP7182AUJZ5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ADP7182AUJZ-1.8', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADP7182AUJZ-5.0', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TSOT-23-5', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/ADP7182.pdf', 'kicadSymbolki_keywords': 'linear regulator ldo fixed negative', 'kicadSymbolki_description': '200mA, Low Noise, CMOS Low Dropout Regulator, Negative, -5.0V Fixed Output, TSOT-23-5', 'kicadSymbolki_fp_filters': 'TSOT?23*'}])
    newPart['name'].append('Regulator_Linear : ADP7182AUJZ-5.0')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

