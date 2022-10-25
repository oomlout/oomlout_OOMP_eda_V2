
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "TLV73328PDBV"
    hexID = "SZKREGULATORLINEARTLV73328PDBV"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LD39015M08R', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TLV73328PDBV', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tlv733p.pdf', 'kicadSymbolki_keywords': '300mA LDO Regulator Fixed Positive Capacitor-Free', 'kicadSymbolki_description': '300mA Capacitor-Free Low Dropout Voltage Regulator, Fixed Output 2.8V, SOT-23-5', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Regulator_Linear : TLV73328PDBV')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

