
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "TLV70013_SOT23-5"
    hexID = "SZKREGULATORLINEARTLV713SOT235"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TLV70012_SOT23-5', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TLV70013_SOT23-5', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tlv700.pdf', 'kicadSymbolki_keywords': '200mA LDO Regulator Fixed Positive', 'kicadSymbolki_description': '200mA Low Dropout Voltage Regulator, Fixed Output 1.3V, SOT-23-5', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Regulator_Linear : TLV70013_SOT23-5')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

