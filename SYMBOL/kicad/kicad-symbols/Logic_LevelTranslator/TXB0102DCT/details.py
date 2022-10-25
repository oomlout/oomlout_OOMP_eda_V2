
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Logic_LevelTranslator"
    oIndex = "TXB0102DCT"
    hexID = "SZKLOGICLEVELTRANSLATORTXB12DCT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TXB0102DCT', 'kicadSymbolFootprint': 'Package_SO:TSSOP-8_3x3mm_P0.65mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/txb0102.pdf', 'kicadSymbolki_keywords': 'Level-Shifter CMOS-TTL-Translation', 'kicadSymbolki_description': '2-Bit Bidirectional Voltage-Level Translator in TSSOP Package With Auto Direction Sensing and ±15-kV ESD Protection', 'kicadSymbolki_fp_filters': 'TSSOP*P0.65mm*'}])
    newPart['name'].append('Logic_LevelTranslator : TXB0102DCT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

