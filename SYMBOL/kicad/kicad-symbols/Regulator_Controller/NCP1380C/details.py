
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Controller"
    oIndex = "NCP1380C"
    hexID = "SZKREGULATORCONTROLLERNCP138C"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'NCP1380A', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NCP1380C', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/NCP1380-D.PDF', 'kicadSymbolki_keywords': 'SMPS Controller AC-DC', 'kicadSymbolki_description': 'Quasi-Resonant Current-Mode Controller for Off-Line Supplies, UVP/OVP, Latched OCP, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Regulator_Controller : NCP1380C')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

