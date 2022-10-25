
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "LTC6253xMS8"
    hexID = "SZKAMPLIFIEROPERATIONALLTC6253XMS8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'NCS2325DM', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC6253xMS8', 'kicadSymbolFootprint': 'Package_SO:MSOP-8_3x3mm_P0.65mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/625234fc.pdf', 'kicadSymbolki_keywords': 'dual opamp low-power', 'kicadSymbolki_description': '720MHz, 3.5mA Power Efficient, Rail-to-Rail Op Amp, MSOP-8', 'kicadSymbolki_fp_filters': 'MSOP*3x3mm*P0.65mm*'}])
    newPart['name'].append('Amplifier_Operational : LTC6253xMS8')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

