
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Logic_LevelTranslator"
    oIndex = "TXBN0304RUT"
    hexID = "SZKLOGICLEVELTRANSLATORTXBN34RUT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TXBN0304RUT', 'kicadSymbolFootprint': 'Package_DFN_QFN:Texas_R_PUQFN-N12', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/txb0304.pdf', 'kicadSymbolki_keywords': 'Level-Shifter CMOS-TTL-Translation', 'kicadSymbolki_description': '4-Bit Bidirectional Voltage-Level Translator, Auto Direction Sensing, 0.9 - 3.6V APort, 0.9 - 3.6V BPort, Active Low Output Enable, Texas_PUQFN-12', 'kicadSymbolki_fp_filters': 'Texas*R*PUQFN*N12*'}])
    newPart['name'].append('TXBN0304RUT')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

