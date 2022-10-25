
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LT1175-ADJ_TO263_TO220"
    hexID = "SZKREGULATORLINEARLT1175ADJTO263TO22"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LT1175-5_TO263_TO220', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT1175-ADJ_TO263_TO220', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/1175ff.pdf', 'kicadSymbolki_keywords': 'linear regulator LDO negative adjustable', 'kicadSymbolki_description': '500mA Negative Low Dropout Micropower Regulator, adjustable output voltage, TO-220-5/TO-263', 'kicadSymbolki_fp_filters': 'TO?263* TO?220*'}])
    newPart['name'].append('Regulator_Linear : LT1175-ADJ_TO263_TO220')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

