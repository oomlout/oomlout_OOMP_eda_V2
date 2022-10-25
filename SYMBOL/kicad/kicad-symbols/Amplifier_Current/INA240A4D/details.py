
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Current"
    oIndex = "INA240A4D"
    hexID = "SZKAMPLIFIERCURRENTINA24A4D"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'INA240A1D', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'INA240A4D', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/ina240.pdf', 'kicadSymbolki_keywords': 'current monitor shunt sensor bidirectional high low', 'kicadSymbolki_description': 'High- and Low-Side, Bidirectional, Zero-Drift, Current-Sense Amplifier With Enhanced PWM Rejection, 200V/V, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Amplifier_Current : INA240A4D')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

