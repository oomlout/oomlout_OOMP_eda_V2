
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Logic_LevelTranslator"
    oIndex = "TXS0102DCT"
    hexID = "SZKLOGICLEVELTRANSLATORTXS12DCT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TXS0102DCT', 'kicadSymbolFootprint': 'Package_SO:SSOP-8_2.95x2.8mm_P0.65mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/gpn/txs0102', 'kicadSymbolki_keywords': 'Level-Shifter CMOS-TTL-Translation', 'kicadSymbolki_description': '2-Bit Bidirectional Voltage-Level Shifter for Open-Drain and Push-Pull Application, SSOP-8', 'kicadSymbolki_fp_filters': 'SSOP*2.95x2.8mm*P0.65mm*'}])
    newPart['name'].append('Logic_LevelTranslator : TXS0102DCT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

