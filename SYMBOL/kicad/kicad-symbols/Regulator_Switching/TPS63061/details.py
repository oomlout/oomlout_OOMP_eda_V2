
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "TPS63061"
    hexID = "SZKREGULATORSWITCHINGTPS6361"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS63061', 'kicadSymbolFootprint': 'Package_SON:Texas_S-PWSON-N10_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tps63060.pdf', 'kicadSymbolki_keywords': 'Buck-Boost converter 5V', 'kicadSymbolki_description': 'Buck-Boost Converter, 2.5-12V Input Voltage, 2-A Switch Current, Fixed 5V Output Voltage, S-PWSON-10', 'kicadSymbolki_fp_filters': 'Texas*S*PWSON*N10*'}])
    newPart['name'].append('Regulator_Switching : TPS63061')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

