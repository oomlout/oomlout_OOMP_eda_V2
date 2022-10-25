
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "TPS73133DBV"
    hexID = "SZKREGULATORLINEARTPS73133DBV"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TPS73625DBV', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS73133DBV', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tps731.pdf', 'kicadSymbolki_keywords': 'Cap free Fixed LDO 150mA', 'kicadSymbolki_description': 'Cap free NMOS 150mA Low Drop 3.3V Regulator, SOT-23-5', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Regulator_Linear : TPS73133DBV')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

