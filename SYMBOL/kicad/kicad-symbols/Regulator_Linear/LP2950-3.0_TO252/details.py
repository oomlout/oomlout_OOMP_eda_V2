
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LP2950-3.0_TO252"
    hexID = "SZKREGULATORLINEARLP2953TO252"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM78M05_TO252', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LP2950-3.0_TO252', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-252-2', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lp2950.pdf', 'kicadSymbolki_keywords': 'Micropower Voltage Regulator 100mA Positive', 'kicadSymbolki_description': 'Positive 100mA 30V Linear Micropower Voltage Regulator, Fixed Output 3.0V, TO-252', 'kicadSymbolki_fp_filters': 'TO?252*'}])
    newPart['name'].append('Regulator_Linear : LP2950-3.0_TO252')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

