
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Controller"
    oIndex = "UCC256301"
    hexID = "SZKREGULATORCONTROLLERUCC25631"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'UCC256301', 'kicadSymbolFootprint': 'Package_SO:SOIC-14-16_3.9x9.9mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/ucc256301.pdf', 'kicadSymbolki_keywords': 'SMPS PWM Controller', 'kicadSymbolki_description': 'Hybrid Hysteretic LLC Resonant Controller, SOIC-16', 'kicadSymbolki_fp_filters': 'SOIC*3.9x9.9mm*P1.27mm*'}])
    newPart['name'].append('Regulator_Controller : UCC256301')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

