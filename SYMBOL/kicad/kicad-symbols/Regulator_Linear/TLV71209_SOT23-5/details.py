
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "TLV71209_SOT23-5"
    hexID = "SZKREGULATORLINEARTLV7129SOT235"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TLV70012_SOT23-5', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TLV71209_SOT23-5', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tlv712.pdf', 'kicadSymbolki_keywords': 'LDO Regulator Fixed Positive', 'kicadSymbolki_description': '300mA Low Dropout Voltage Regulator, Fixed Output 0.9V, SOT-23-5', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Regulator_Linear : TLV71209_SOT23-5')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

