
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "LTC6268xS8-10"
    hexID = "SZKAMPLIFIEROPERATIONALLTC6268XS81"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC6268xS8-10', 'kicadSymbolFootprint': 'Package_SO:SO-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/626810f.pdf', 'kicadSymbolki_keywords': 'single opamp transimpedance', 'kicadSymbolki_description': '4GHz, Ultra-Low Bias Current, FET Input, Op Amp, SOIC-8', 'kicadSymbolki_fp_filters': 'SO*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Amplifier_Operational : LTC6268xS8-10')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

