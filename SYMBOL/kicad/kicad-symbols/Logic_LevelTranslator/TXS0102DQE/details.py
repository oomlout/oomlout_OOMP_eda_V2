
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Logic_LevelTranslator"
    oIndex = "TXS0102DQE"
    hexID = "SZKLOGICLEVELTRANSLATORTXS12DQE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TXS0102DQE', 'kicadSymbolFootprint': 'Package_SON:X2SON-8_1.4x1mm_P0.35mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/gpn/txs0102', 'kicadSymbolki_keywords': 'Level-Shifter CMOS-TTL-Translation', 'kicadSymbolki_description': '2-Bit Bidirectional Voltage-Level Shifter for Open-Drain and Push-Pull Application, X2SON-8', 'kicadSymbolki_fp_filters': 'X2SON*1.4x1mm*P0.35mm*'}])
    newPart['name'].append('Logic_LevelTranslator : TXS0102DQE')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

