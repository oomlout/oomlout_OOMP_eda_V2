
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Reference_Voltage"
    oIndex = "LT6657BHMS8-3"
    hexID = "SZKREFERENCEVOLTAGELT6657BHMS83"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LT6657AHMS8-2.5', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT6657BHMS8-3', 'kicadSymbolFootprint': 'Package_SO:MSOP-8_3x3mm_P0.65mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/6657fd.pdf', 'kicadSymbolki_keywords': 'voltage reference vref', 'kicadSymbolki_description': 'Precision voltage reference, 40V input, 10mA output, 3.0ppm/C drift, 3.0V output, MSOP-8', 'kicadSymbolki_fp_filters': 'MSOP*3x3mm*P0.65mm*'}])
    newPart['name'].append('Reference_Voltage : LT6657BHMS8-3')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

