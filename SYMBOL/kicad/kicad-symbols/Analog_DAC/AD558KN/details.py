
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_DAC"
    oIndex = "AD558KN"
    hexID = "SZKANALOGDACAD558KN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AD558JN', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD558KN', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/static/imported-files/data_sheets/AD558.pdf', 'kicadSymbolki_keywords': '8bit DAC Reference Single Supply', 'kicadSymbolki_description': 'Single 8-bit DAC, Internal Reference, Output Amp, Single Supply, DIP-16', 'kicadSymbolki_fp_filters': 'DIP* PDIP*'}])
    newPart['name'].append('Analog_DAC : AD558KN')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

