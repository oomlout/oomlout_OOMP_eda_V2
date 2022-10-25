
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Logic_LevelTranslator"
    oIndex = "TXB0104ZXU"
    hexID = "SZKLOGICLEVELTRANSLATORTXB14ZXU"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TXB0104ZXU', 'kicadSymbolFootprint': 'Package_BGA:Texas_MicroStar_Junior_BGA-12_2.0x2.5mm_Layout4x3_P0.5mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/txb0104.pdf', 'kicadSymbolki_keywords': 'Level-Shifter CMOS-TTL-Translation', 'kicadSymbolki_description': '4-Bit Bidirectional Voltage-Level Translator, Auto Direction Sensing and ±15-kV ESD Protection, 1.2 - 3.6V APort, 1.65 - 5.5V BPort, Texas_Junior-12', 'kicadSymbolki_fp_filters': 'Texas*Junior*BGA*2.0x2.5mm*Layout4x3*P0.5mm*'}])
    newPart['name'].append('Logic_LevelTranslator : TXB0104ZXU')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

