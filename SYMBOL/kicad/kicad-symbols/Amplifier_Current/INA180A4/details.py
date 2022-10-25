
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Current"
    oIndex = "INA180A4"
    hexID = "SZKAMPLIFIERCURRENTINA18A4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'INA180A1', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'INA180A4', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/ina180.pdf', 'kicadSymbolki_keywords': 'current monitor shunt sensor', 'kicadSymbolki_description': 'Current Sense Amplifier, 1 Circuit, Rail-to-Rail, 26V, Gain 200 V/V, SOT-23-5', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Amplifier_Current : INA180A4')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

