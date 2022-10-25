
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Logic_LevelTranslator"
    oIndex = "SN74LVC2T45DCUR"
    hexID = "SZKLOGICLEVELTRANSLATORSN74LVC2T45DCUR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SN74LVC2T45DCUR', 'kicadSymbolFootprint': 'Package_SO:VSSOP-8_2.4x2.1mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/sn74lvc2t45.pdf', 'kicadSymbolki_keywords': 'Level-Shifter CMOS-TTL-Translation', 'kicadSymbolki_description': 'Dual-Bit Dual-Supply Bus Transceiver With Configurable Voltage Translation and 3-State Outputs, VSSOP-8', 'kicadSymbolki_fp_filters': 'VSSOP*2.4x2.1mm*P0.5mm*'}])
    newPart['name'].append('Logic_LevelTranslator : SN74LVC2T45DCUR')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

