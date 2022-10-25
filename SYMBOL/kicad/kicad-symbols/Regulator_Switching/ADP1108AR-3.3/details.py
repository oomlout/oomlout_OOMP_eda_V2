
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "ADP1108AR-3.3"
    hexID = "SZKREGULATORSWITCHINGADP118AR33"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LT1073CS-5', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADP1108AR-3.3', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/ADP1108.pdf', 'kicadSymbolki_keywords': 'switching buck boost converter step-down step-up', 'kicadSymbolki_description': 'Micropower DC-DC converter, step-up or step-down operation, 2V-30Vin, 3.3V fixed output voltage, DIP-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Regulator_Switching : ADP1108AR-3.3')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

