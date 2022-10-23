
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LT1175-ADJ_SO8_DIP8"
    hexID = "SZKREGULATORLINEARLT1175ADJSO8DIP8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LT1175-5_SO8_DIP8', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT1175-ADJ_SO8_DIP8', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/1175ff.pdf', 'kicadSymbolki_keywords': 'linear regulator LDO negative adjustable', 'kicadSymbolki_description': '500mA Negative Low Dropout Micropower Regulator, adjustable output voltage, SO-8/DIP-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm* DIP*W7.62mm*'}])
    newPart['name'].append('LT1175-ADJ_SO8_DIP8')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

