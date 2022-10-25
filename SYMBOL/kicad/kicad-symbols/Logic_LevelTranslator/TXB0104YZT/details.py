
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Logic_LevelTranslator"
    oIndex = "TXB0104YZT"
    hexID = "SZKLOGICLEVELTRANSLATORTXB14YZT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TXB0104YZT', 'kicadSymbolFootprint': 'Package_BGA:Texas_DSBGA-12_1.36x1.86mm_Layout3x4_P0.5mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/txb0104.pdf', 'kicadSymbolki_keywords': 'Level-Shifter CMOS-TTL-Translation', 'kicadSymbolki_description': '4-Bit Bidirectional Voltage-Level Translator, Auto Direction Sensing and ±15-kV ESD Protection, 1.2 - 3.6V APort, 1.65 - 5.5V BPort, DSBGA-12', 'kicadSymbolki_fp_filters': 'Texas*DSBGA*1.36x1.86mm*Layout3x4*P0.5mm*'}])
    newPart['name'].append('Logic_LevelTranslator : TXB0104YZT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

