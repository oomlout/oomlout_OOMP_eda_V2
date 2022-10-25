
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Logic_LevelTranslator"
    oIndex = "TXB0102DCU"
    hexID = "SZKLOGICLEVELTRANSLATORTXB12DCU"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TXB0102DCU', 'kicadSymbolFootprint': 'Package_SO:VSSOP-8_2.4x2.1mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/txb0102.pdf', 'kicadSymbolki_keywords': 'Level-Shifter CMOS-TTL-Translation', 'kicadSymbolki_description': '2-Bit Bidirectional Voltage-Level Translator in VSSOP Package With Auto Direction Sensing and ±15-kV ESD Protection', 'kicadSymbolki_fp_filters': 'VSSOP*P0.5mm*'}])
    newPart['name'].append('Logic_LevelTranslator : TXB0102DCU')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

