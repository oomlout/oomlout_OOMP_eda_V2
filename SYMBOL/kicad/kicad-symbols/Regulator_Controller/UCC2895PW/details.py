
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Controller"
    oIndex = "UCC2895PW"
    hexID = "SZKREGULATORCONTROLLERUCC2895PW"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'UCC3895PW', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'UCC2895PW', 'kicadSymbolFootprint': 'Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/ucc3895.pdf', 'kicadSymbolki_keywords': 'Phase-shift full-bridge converter', 'kicadSymbolki_description': 'BiCMOS, Advanced Phase-ShiftPWM Controller, TSSOP-20', 'kicadSymbolki_fp_filters': 'TSSOP*4.4x6.5mm*P0.65mm*'}])
    newPart['name'].append('Regulator_Controller : UCC2895PW')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

