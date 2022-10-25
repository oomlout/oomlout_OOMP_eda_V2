
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Current"
    oIndex = "INA169"
    hexID = "SZKAMPLIFIERCURRENTINA169"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'INA138', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'INA169', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/ina169.pdf', 'kicadSymbolki_keywords': 'current sense shunt monitor', 'kicadSymbolki_description': 'High-Side Measurement Current Shunt Monitor, 60V, SOT-23-5', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Amplifier_Current : INA169')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

