
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Controller"
    oIndex = "UC3527"
    hexID = "SZKREGULATORCONTROLLERUC3527"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'UC3525', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'UC3527', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/uc2525b.pdf', 'kicadSymbolki_keywords': 'SMPS PWM Controller', 'kicadSymbolki_description': 'Regulating Pulse Width Modulators, OR Logic, PDIP-16/SOIC-16', 'kicadSymbolki_fp_filters': 'SOIC*16*7.5x10.3mm*P1.27mm* DIP*16*W7.62mm*'}])
    newPart['name'].append('Regulator_Controller : UC3527')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

