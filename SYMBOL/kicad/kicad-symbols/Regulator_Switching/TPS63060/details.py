
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "TPS63060"
    hexID = "SZKREGULATORSWITCHINGTPS636"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS63060', 'kicadSymbolFootprint': 'Package_SON:Texas_S-PWSON-N10_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tps63060.pdf', 'kicadSymbolki_keywords': 'Buck-Boost adjustable converter', 'kicadSymbolki_description': 'Buck-Boost Converter, 2.5-12V Input Voltage, 2-A Switch Current, Adjustable 2.5-8V Output Voltage, S-PWSON-N10', 'kicadSymbolki_fp_filters': 'Texas*S*PWSON*N10*'}])
    newPart['name'].append('Regulator_Switching : TPS63060')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

