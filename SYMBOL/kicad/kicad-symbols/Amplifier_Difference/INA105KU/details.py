
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Difference"
    oIndex = "INA105KU"
    hexID = "SZKAMPLIFIERDIFFERENCEINA15KU"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AD8276', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'INA105KU', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/ina105.pdf', 'kicadSymbolki_keywords': 'difference amplifier', 'kicadSymbolki_description': 'Low Power, Wide Supply Range, Low Cost Unity-Gain Difference Amplifier, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Amplifier_Difference : INA105KU')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

