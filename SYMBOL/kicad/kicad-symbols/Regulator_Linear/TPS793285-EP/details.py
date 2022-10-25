
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "TPS793285-EP"
    hexID = "SZKREGULATORLINEARTPS793285EP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TPS79318-EP', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS793285-EP', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tps79333-ep.pdf', 'kicadSymbolki_keywords': 'LDO Voltage Regulator 200mA', 'kicadSymbolki_description': '200mA UltraLow-Noise, High-Precision, Fast RF, Low Drop-out Voltage Regulator, Fixed Output 2.85V, SOT-23', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Regulator_Linear : TPS793285-EP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

