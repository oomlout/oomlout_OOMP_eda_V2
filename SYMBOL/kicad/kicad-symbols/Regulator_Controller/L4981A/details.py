
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Controller"
    oIndex = "L4981A"
    hexID = "SZKREGULATORCONTROLLERL4981A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'L4981A', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.st.com/resource/en/datasheet/l4981.pdf', 'kicadSymbolki_keywords': 'SMPS pfc controller', 'kicadSymbolki_description': 'Power Factor Corrector, Fixed Frequency Average Current Mode, DIP-20/SOIC-20', 'kicadSymbolki_fp_filters': 'SOIC*7.5x12.8mm*P1.27mm* DIP*W7.62mm*'}])
    newPart['name'].append('Regulator_Controller : L4981A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

