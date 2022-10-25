
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Logic_LevelTranslator"
    oIndex = "TXB0104D"
    hexID = "SZKLOGICLEVELTRANSLATORTXB14D"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TXB0104D', 'kicadSymbolFootprint': 'Package_SO:SOIC-14_3.9x8.7mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/txb0104.pdf', 'kicadSymbolki_keywords': 'Level-Shifter CMOS-TTL-Translation', 'kicadSymbolki_description': '4-Bit Bidirectional Voltage-Level Translator, Auto Direction Sensing and ±15-kV ESD Protection, 1.2 - 3.6V APort, 1.65 - 5.5V BPort, SOIC-14', 'kicadSymbolki_fp_filters': 'SOIC*14*7mm*P1.27mm*'}])
    newPart['name'].append('Logic_LevelTranslator : TXB0104D')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

