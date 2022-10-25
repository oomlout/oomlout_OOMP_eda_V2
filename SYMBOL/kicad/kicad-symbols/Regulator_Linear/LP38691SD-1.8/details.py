
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LP38691SD-1.8"
    hexID = "SZKREGULATORLINEARLP38691SD18"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LP38691SD-1.8', 'kicadSymbolFootprint': 'Package_SON:WSON-6-1EP_3x3mm_P0.95mm', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/lp38691.pdf', 'kicadSymbolki_keywords': 'LDO Linear Regulator', 'kicadSymbolki_description': '500-mA Low-Dropout CMOS Linear Regulators Stable With Ceramic Output Capacitors, 1.8V output voltage, WSON-6', 'kicadSymbolki_fp_filters': 'WSON*1EP*3x3mm*P0.95mm*'}])
    newPart['name'].append('Regulator_Linear : LP38691SD-1.8')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

