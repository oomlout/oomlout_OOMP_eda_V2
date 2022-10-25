
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LP2980-ADJ"
    hexID = "SZKREGULATORLINEARLP298ADJ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LP2980-ADJ', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lp2980-adj.pdf', 'kicadSymbolki_keywords': 'LDO Voltage Regulator 50mA Positive', 'kicadSymbolki_description': '50mA 15V Low-noise Low-dropout Regulator, 1.23-15V adjustable output voltage, SOT-23-5', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Regulator_Linear : LP2980-ADJ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

