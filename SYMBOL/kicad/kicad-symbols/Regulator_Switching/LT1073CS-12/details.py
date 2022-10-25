
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LT1073CS-12"
    hexID = "SZKREGULATORSWITCHINGLT173CS12"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LT1073CS-5', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT1073CS-12', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/1073fa.pdf', 'kicadSymbolki_keywords': 'Micropower DC/DC Converter', 'kicadSymbolki_description': 'Micropower DC/DC Converter, Fixed 12V Output Voltage, SO-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Regulator_Switching : LT1073CS-12')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

