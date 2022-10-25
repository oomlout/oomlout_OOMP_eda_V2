
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LT3093xMSE"
    hexID = "SZKREGULATORLINEARLT393XMSE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT3093xMSE', 'kicadSymbolFootprint': 'Package_SO:MSOP-12-1EP_3x4mm_P0.65mm_EP1.65x2.85mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/lt3093.pdf', 'kicadSymbolki_keywords': 'linear negative voltage regulator low-noise', 'kicadSymbolki_description': '-200mA, Adjustable, Ultralow Noise, Ultrahigh PSRR RF Negative Linear Regulator, MSOP-12', 'kicadSymbolki_fp_filters': 'MSOP*1EP*3x4mm*P0.65mm*'}])
    newPart['name'].append('Regulator_Linear : LT3093xMSE')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

