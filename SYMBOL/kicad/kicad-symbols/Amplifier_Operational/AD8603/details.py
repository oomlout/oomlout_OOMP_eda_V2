
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "AD8603"
    hexID = "SZKAMPLIFIEROPERATIONALAD863"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD8603', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TSOT-23-5', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/AD8603_8607_8609.pdf', 'kicadSymbolki_keywords': 'single opamp', 'kicadSymbolki_description': 'Precision Micropower, Low Noise CMOS, Rail-to-Rail Input/Output Operational Amplifier, TSOT-23-5', 'kicadSymbolki_fp_filters': 'TSOT*23*'}])
    newPart['name'].append('Amplifier_Operational : AD8603')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

