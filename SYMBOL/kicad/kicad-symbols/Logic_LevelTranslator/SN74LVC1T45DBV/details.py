
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Logic_LevelTranslator"
    oIndex = "SN74LVC1T45DBV"
    hexID = "SZKLOGICLEVELTRANSLATORSN74LVC1T45DBV"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SN74LVC1T45DBV', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-6', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/sn74lvc1t45.pdf', 'kicadSymbolki_keywords': 'Level-Shifter CMOS-TTL-Translation', 'kicadSymbolki_description': 'Single-Bit Dual-Supply Bus Transceiver With Configurable Voltage Translation and 3-State Outputs, SOT-23-6', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Logic_LevelTranslator : SN74LVC1T45DBV')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

