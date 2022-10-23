
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Logic_LevelTranslator"
    oIndex = "SN74LVC2T45YZP"
    hexID = "SZKLOGICLEVELTRANSLATORSN74LVC2T45YZP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SN74LVC2T45YZP', 'kicadSymbolFootprint': 'Package_BGA:Texas_DSBGA-8_0.9x1.9mm_Layout2x4_P0.5mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/sn74lvc2t45.pdf', 'kicadSymbolki_keywords': 'Level-Shifter CMOS-TTL-Translation', 'kicadSymbolki_description': 'Dual-Bit Dual-Supply Bus Transceiver With Configurable Voltage Translation and 3-State Outputs, DSBGA-8', 'kicadSymbolki_fp_filters': 'Texas*DSBGA*0.9x1.9mm*Layout2x4*P0.5mm*'}])
    newPart['name'].append('SN74LVC2T45YZP')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

