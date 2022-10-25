
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "TLV75525PDRV"
    hexID = "SZKREGULATORLINEARTLV75525PDRV"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TLV75509PDRV', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TLV75525PDRV', 'kicadSymbolFootprint': 'Package_SON:WSON-6-1EP_2x2mm_P0.65mm_EP1x1.6mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tlv755p.pdf', 'kicadSymbolki_keywords': 'LDO Regulator Fixed Positive', 'kicadSymbolki_description': '500mA Low Dropout Voltage Regulator, Fixed Output 2.5V, WSON6', 'kicadSymbolki_fp_filters': 'WSON*1EP*2x2mm*P0.65mm*'}])
    newPart['name'].append('Regulator_Linear : TLV75525PDRV')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

