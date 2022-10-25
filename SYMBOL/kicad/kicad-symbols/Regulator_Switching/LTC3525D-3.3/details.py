
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LTC3525D-3.3"
    hexID = "SZKREGULATORSWITCHINGLTC3525D33"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LTC3525', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC3525D-3.3', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/3525d33fb.pdf', 'kicadSymbolki_keywords': 'fixed boost step-up DC/DC synchronous', 'kicadSymbolki_description': 'Fixed 3V3, 400mA Micropower Synchronous Step-Up DC/DC Converter with Pass Through Mode, SC-70-6', 'kicadSymbolki_fp_filters': '*SC?70* SOT?363*'}])
    newPart['name'].append('Regulator_Switching : LTC3525D-3.3')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

