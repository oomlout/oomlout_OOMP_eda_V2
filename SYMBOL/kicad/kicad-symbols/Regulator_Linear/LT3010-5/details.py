
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LT3010-5"
    hexID = "SZKREGULATORLINEARLT315"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT3010-5', 'kicadSymbolFootprint': 'Package_SO:MSOP-8-1EP_3x3mm_P0.65mm_EP1.68x1.88mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/30105fe.pdf', 'kicadSymbolki_keywords': 'REGULATOR POSITIVE POWER LDO fixed', 'kicadSymbolki_description': '50mA 3-80V Micropower Low Dropout Regulator, fixed output 5V, MSOP-8', 'kicadSymbolki_fp_filters': 'MSOP*3x3mm*P0.65mm*'}])
    newPart['name'].append('Regulator_Linear : LT3010-5')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

