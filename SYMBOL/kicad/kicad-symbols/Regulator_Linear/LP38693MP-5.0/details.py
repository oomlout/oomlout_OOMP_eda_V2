
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LP38693MP-5.0"
    hexID = "SZKREGULATORLINEARLP38693MP5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LP38693MP-1.8', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LP38693MP-5.0', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-223-5', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/lp38693.pdf', 'kicadSymbolki_keywords': 'LDO Linear Regulator', 'kicadSymbolki_description': '500-mA Low-Dropout CMOS Linear Regulators Stable With Ceramic Output Capacitors, 5.0V output voltage, Enable Pin, SOT-223', 'kicadSymbolki_fp_filters': 'SOT*223*'}])
    newPart['name'].append('Regulator_Linear : LP38693MP-5.0')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

