
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "TPS78228DDC"
    hexID = "SZKREGULATORLINEARTPS78228DDC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TPS78233DDC', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS78228DDC', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/gpn/tps782', 'kicadSymbolki_keywords': 'Single Output LDO Low-Iq', 'kicadSymbolki_description': '150-mA, 500nA Ultra-Low-IQ LDO, 2.8V, SOT-23-5', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Regulator_Linear : TPS78228DDC')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

