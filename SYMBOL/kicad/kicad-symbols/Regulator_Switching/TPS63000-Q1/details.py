
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "TPS63000-Q1"
    hexID = "SZKREGULATORSWITCHINGTPS63Q1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TPS63000', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS63000-Q1', 'kicadSymbolFootprint': 'Package_SON:Texas_DRC0010J_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tps63000-q1.pdf', 'kicadSymbolki_keywords': 'Buck-Boost adjustable converter', 'kicadSymbolki_description': 'Buck-Boost Converter, 1.8-5.5V Input Voltage, 1.8A Switch Current, Adjustable 1.2-5.5V Output Voltage, Automotive, VSON-10', 'kicadSymbolki_fp_filters': 'Texas*DRC0010J*'}])
    newPart['name'].append('Regulator_Switching : TPS63000-Q1')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

