
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "ADP2108AUJ-1.3"
    hexID = "SZKREGULATORSWITCHINGADP218AUJ13"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ADP2108AUJ-1.0', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADP2108AUJ-1.3', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TSOT-23-5', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/ADP2108.pdf', 'kicadSymbolki_keywords': 'Voltage regulator switching buck fixed output analog', 'kicadSymbolki_description': '3MHz switching bucK regulator, 600mA 1.3V output voltage,', 'kicadSymbolki_fp_filters': 'TSOT?23*'}])
    newPart['name'].append('Regulator_Switching : ADP2108AUJ-1.3')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

