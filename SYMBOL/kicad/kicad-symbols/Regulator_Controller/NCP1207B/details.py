
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Controller"
    oIndex = "NCP1207B"
    hexID = "SZKREGULATORCONTROLLERNCP127B"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NCP1207B', 'kicadSymbolFootprint': 'Package_SO:SOIC-8-N7_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub/Collateral/NCP1207B.PDF', 'kicadSymbolki_keywords': 'SMPS Controller AC-DC', 'kicadSymbolki_description': 'PWM Current-Mode Controller for Free Running Quasi-Resonant Operation, AC-DC, 4.5us min Toff, SOIC-7', 'kicadSymbolki_fp_filters': 'SOIC*N7*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Regulator_Controller : NCP1207B')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

