
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Reference_Voltage"
    oIndex = "LT1461CxS8-5"
    hexID = "SZKREFERENCEVOLTAGELT1461CXS85"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LT1461AxS8-2.5', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT1461CxS8-5', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/LT1461.pdf', 'kicadSymbolki_keywords': 'voltage reference precision', 'kicadSymbolki_description': 'Voltage Reference, +/-0.08%, 5V, 100mA, 5.5V-20V Vin, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Reference_Voltage : LT1461CxS8-5')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

