
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Logic_LevelTranslator"
    oIndex = "TXB0104RUT"
    hexID = "SZKLOGICLEVELTRANSLATORTXB14RUT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TXB0104RUT', 'kicadSymbolFootprint': 'Package_DFN_QFN:Texas_R_PUQFN-N12', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/txb0104.pdf', 'kicadSymbolki_keywords': 'Level-Shifter CMOS-TTL-Translation', 'kicadSymbolki_description': '4-Bit Bidirectional Voltage-Level Translator, Auto Direction Sensing and ±15-kV ESD Protection, 1.2 - 3.6V APort, 1.65 - 5.5V BPort, Texas_PUQFN-12', 'kicadSymbolki_fp_filters': 'Texas*R*PUQFN*N12*'}])
    newPart['name'].append('Logic_LevelTranslator : TXB0104RUT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

