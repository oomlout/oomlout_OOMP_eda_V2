
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Logic_LevelTranslator"
    oIndex = "TXS0102YZP"
    hexID = "SZKLOGICLEVELTRANSLATORTXS12YZP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TXS0102YZP', 'kicadSymbolFootprint': 'Package_BGA:Texas_DSBGA-8_0.9x1.9mm_Layout2x4_P0.5mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/gpn/txs0102', 'kicadSymbolki_keywords': 'Level-Shifter CMOS-TTL-Translation', 'kicadSymbolki_description': '2-Bit Bidirectional Voltage-Level Shifter for Open-Drain and Push-Pull Application, DSBGA-8', 'kicadSymbolki_fp_filters': 'Texas*DSBGA*0.9x1.9mm*Layout2x4*P0.5mm*'}])
    newPart['name'].append('TXS0102YZP')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

