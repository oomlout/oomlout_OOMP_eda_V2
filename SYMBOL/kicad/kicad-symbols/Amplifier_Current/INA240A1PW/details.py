
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Current"
    oIndex = "INA240A1PW"
    hexID = "SZKAMPLIFIERCURRENTINA24A1PW"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'INA240A1PW', 'kicadSymbolFootprint': 'Package_SO:TSSOP-8_4.4x3mm_P0.65mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/ina240.pdf', 'kicadSymbolki_keywords': 'current monitor shunt sensor bidirectional high low', 'kicadSymbolki_description': 'High- and Low-Side, Bidirectional, Zero-Drift, Current-Sense Amplifier With Enhanced PWM Rejection, 20V/V, TSSOP-8', 'kicadSymbolki_fp_filters': 'TSSOP*4.4x3mm*P0.65mm*'}])
    newPart['name'].append('Amplifier_Current : INA240A1PW')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

