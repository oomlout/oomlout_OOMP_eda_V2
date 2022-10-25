
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "TPS76338"
    hexID = "SZKREGULATORLINEARTPS76338"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TPS76316', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS76338', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tps763.pdf', 'kicadSymbolki_keywords': 'linear low dropout Regulator fixed', 'kicadSymbolki_description': 'Low power 150mA LDO 3.8V fixed output voltage, SOT-23-5', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Regulator_Linear : TPS76338')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

