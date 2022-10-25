
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "ADA4807-1"
    hexID = "SZKAMPLIFIEROPERATIONALADA4871"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADA4807-1', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/ADA4807-1_4807-2_4807-4.pdf', 'kicadSymbolki_keywords': 'single opamp', 'kicadSymbolki_description': 'Single Rail-to-Rail Input/Output Amplifiers, with disable, SC-70-6/SOT-23-6', 'kicadSymbolki_fp_filters': '*SC*70* SOT?23*'}])
    newPart['name'].append('Amplifier_Operational : ADA4807-1')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

