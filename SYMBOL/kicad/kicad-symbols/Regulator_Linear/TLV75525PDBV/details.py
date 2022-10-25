
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "TLV75525PDBV"
    hexID = "SZKREGULATORLINEARTLV75525PDBV"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TLV70012_SOT23-5', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TLV75525PDBV', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tlv755p.pdf', 'kicadSymbolki_keywords': 'LDO Regulator Fixed Positive', 'kicadSymbolki_description': '500mA Low Dropout Voltage Regulator, Fixed Output 2.5V, SOT-23-5', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Regulator_Linear : TLV75525PDBV')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

