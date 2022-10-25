
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Current"
    oIndex = "INA286"
    hexID = "SZKAMPLIFIERCURRENTINA286"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'INA282', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'INA286', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/ina282.pdf', 'kicadSymbolki_keywords': 'current monitor shunt sensor bidirectional', 'kicadSymbolki_description': 'High-Accuracy, Wide Common-Mode Range, Bidirectional Current Shunt Monitors, Zero-Drift Series, 100V/V, SOIC-8/VSSOP-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm* MSOP*3x3mm*P0.65mm*'}])
    newPart['name'].append('Amplifier_Current : INA286')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

