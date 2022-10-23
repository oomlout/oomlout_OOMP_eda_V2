
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LT3042xMSE"
    hexID = "SZKREGULATORLINEARLT342XMSE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT3042xMSE', 'kicadSymbolFootprint': 'Package_SO:MSOP-10-1EP_3x3mm_P0.5mm_EP1.68x1.88mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/3042fb.pdf', 'kicadSymbolki_keywords': 'linear voltage regulator low-noise', 'kicadSymbolki_description': '200mA, Adjustable, Ultralow Noise, Ultrahigh PSRR RF Linear Regulator, MSOP-10', 'kicadSymbolki_fp_filters': 'MSOP*1EP*3x3mm*P0.5mm*'}])
    newPart['name'].append('LT3042xMSE')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

