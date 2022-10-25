
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Reference_Voltage"
    oIndex = "ADR425ARMZ"
    hexID = "SZKREFERENCEVOLTAGEADR425ARMZ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ADR420ARMZ', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADR425ARMZ', 'kicadSymbolFootprint': 'Package_SO:MSOP-8_3x3mm_P0.65mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/adr420_421_423_425.pdf', 'kicadSymbolki_keywords': '5V voltage reference', 'kicadSymbolki_description': '5.00V Voltage Reference, Ultraprecision, Low Noise, MSOP-8', 'kicadSymbolki_fp_filters': 'MSOP*3x3mm*P0.65mm*'}])
    newPart['name'].append('Reference_Voltage : ADR425ARMZ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

