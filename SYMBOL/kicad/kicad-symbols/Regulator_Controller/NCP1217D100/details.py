
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Controller"
    oIndex = "NCP1217D100"
    hexID = "SZKREGULATORCONTROLLERNCP1217D1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'NCP1200D40', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NCP1217D100', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub_link/Collateral/NCP1217-D.PDF', 'kicadSymbolki_keywords': 'SMPS Controller AC-DC', 'kicadSymbolki_description': 'Enhanced PWM Current-Mode Controller for High-Power Universal Off-Line Supplies, AC-DC, 100kHz, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Regulator_Controller : NCP1217D100')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

