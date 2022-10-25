
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Controller"
    oIndex = "L6561"
    hexID = "SZKREGULATORCONTROLLERL6561"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'L6561', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.st.com/resource/en/datasheet/l6561.pdf', 'kicadSymbolki_keywords': 'SMPS pfc controller', 'kicadSymbolki_description': 'Transition Mode Power Factor Corrector, DIP-8/SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm* DIP*W7.62mm*'}])
    newPart['name'].append('Regulator_Controller : L6561')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

