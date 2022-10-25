
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "TPS7148"
    hexID = "SZKREGULATORLINEARTPS7148"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TPS7150', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS7148', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tps71.pdf', 'kicadSymbolki_keywords': 'LDO Voltage Regulator 500mA', 'kicadSymbolki_description': '500mA Low Drop-out Voltage Regulator, Fixed Output 4.85V, SO-8/DIP-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm* DIP*W7.62mm*'}])
    newPart['name'].append('Regulator_Linear : TPS7148')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

