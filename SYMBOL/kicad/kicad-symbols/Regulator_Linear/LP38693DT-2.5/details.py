
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LP38693DT-2.5"
    hexID = "SZKREGULATORLINEARLP38693DT25"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LP38693DT-1.8', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LP38693DT-2.5', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-252-2', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/lp38693.pdf', 'kicadSymbolki_keywords': 'LDO Linear Regulator', 'kicadSymbolki_description': '500-mA Low-Dropout CMOS Linear Regulators Stable With Ceramic Output Capacitors, 2.5V output voltage, TO-252', 'kicadSymbolki_fp_filters': 'TO*252*'}])
    newPart['name'].append('Regulator_Linear : LP38693DT-2.5')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

