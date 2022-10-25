
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Potentiometer_Digital"
    oIndex = "TPL0401B-10-Q1"
    hexID = "SZKPOTENTIOMETERDIGITALTPL41B1Q1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TPL0401A-10-Q1', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPL0401B-10-Q1', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:Texas_R-PDSO-G6', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tpl0401a-10-q1.pdf', 'kicadSymbolki_keywords': 'Digital Pot Potentiometer I2C', 'kicadSymbolki_description': '128-TAPS Single-Channel Digital Potentiometer, I2C Interface, SC-70-6', 'kicadSymbolki_fp_filters': 'Texas*R*PDSO*G*'}])
    newPart['name'].append('Potentiometer_Digital : TPL0401B-10-Q1')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

