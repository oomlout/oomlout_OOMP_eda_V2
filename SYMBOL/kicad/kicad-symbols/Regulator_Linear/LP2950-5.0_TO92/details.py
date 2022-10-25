
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LP2950-5.0_TO92"
    hexID = "SZKREGULATORLINEARLP2955TO92"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MC78L05_TO92', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LP2950-5.0_TO92', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-92_Inline', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lp2951.pdf', 'kicadSymbolki_keywords': 'Micropower Voltage Regulator 100mA Positive', 'kicadSymbolki_description': 'Micropower Voltage Regulators with Shutdown, 100mA, Fixed Output 5.0V, TO-92', 'kicadSymbolki_fp_filters': 'TO?92*'}])
    newPart['name'].append('Regulator_Linear : LP2950-5.0_TO92')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

