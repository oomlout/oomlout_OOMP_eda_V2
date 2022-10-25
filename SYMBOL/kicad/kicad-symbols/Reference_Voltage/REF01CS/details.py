
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Reference_Voltage"
    oIndex = "REF01CS"
    hexID = "SZKREFERENCEVOLTAGEREF1CS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'REF02AU', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'REF01CS', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/REF01_02_03.pdf', 'kicadSymbolki_keywords': 'Precision Voltage Reference 10V', 'kicadSymbolki_description': '10V ±100mV Precision Voltage Reference, SO-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Reference_Voltage : REF01CS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

