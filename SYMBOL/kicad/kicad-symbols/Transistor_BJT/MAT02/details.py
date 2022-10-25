
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "MAT02"
    hexID = "SZKTRANSISTORBJTMAT2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'MAT02', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-78-6', 'kicadSymbolDatasheet': 'http://www.elenota.pl/datasheet_download/93431/MAT02', 'kicadSymbolki_keywords': 'Precision Dual Monolithic Transistor Low Noise EOL', 'kicadSymbolki_description': '20mA Ic, 40V Vce, Precision Dual Monolithic Low Noise, Low Offset Transistor, TO-78', 'kicadSymbolki_fp_filters': 'TO?78*'}])
    newPart['name'].append('Transistor_BJT : MAT02')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

