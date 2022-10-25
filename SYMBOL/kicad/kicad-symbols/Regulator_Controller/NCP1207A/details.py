
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Controller"
    oIndex = "NCP1207A"
    hexID = "SZKREGULATORCONTROLLERNCP127A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NCP1207A', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub/Collateral/NCP1207B.PDF', 'kicadSymbolki_keywords': 'SMPS Controller AC-DC', 'kicadSymbolki_description': 'PWM Current-Mode Controller for Free Running Quasi-Resonant Operation, AC-DC, 8us min Toff, PDIP-8/SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm* DIP*W7.62mm*'}])
    newPart['name'].append('Regulator_Controller : NCP1207A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

