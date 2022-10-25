
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "TLV70225_SOT23-5"
    hexID = "SZKREGULATORLINEARTLV7225SOT235"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TLV70012_SOT23-5', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TLV70225_SOT23-5', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tlv702.pdf', 'kicadSymbolki_keywords': '300mA LDO Regulator Fixed Positive', 'kicadSymbolki_description': '300mA Low Dropout Voltage Regulator, Fixed Output 2.5V, SOT-23-5', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Regulator_Linear : TLV70225_SOT23-5')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

