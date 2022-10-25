
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "TLV70018_SOT353"
    hexID = "SZKREGULATORLINEARTLV718SOT353"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TLV70012_SOT353', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TLV70018_SOT353', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-353_SC-70-5', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tlv700.pdf', 'kicadSymbolki_keywords': '200mA LDO Regulator Fixed Positive', 'kicadSymbolki_description': '200mA Low Dropout Voltage Regulator, Fixed Output 1.8V, SC70-5', 'kicadSymbolki_fp_filters': 'SOT*353*'}])
    newPart['name'].append('Regulator_Linear : TLV70018_SOT353')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

