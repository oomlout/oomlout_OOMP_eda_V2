
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "TPS76928"
    hexID = "SZKREGULATORLINEARTPS76928"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TPS76912', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS76928', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tps769.pdf', 'kicadSymbolki_keywords': 'Ultra Low Power Fixed LDO 100mA', 'kicadSymbolki_description': 'Ultra Low Power 100mA Low Drop Out Regulator 2.8V, SOT-23-5', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Regulator_Linear : TPS76928')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

