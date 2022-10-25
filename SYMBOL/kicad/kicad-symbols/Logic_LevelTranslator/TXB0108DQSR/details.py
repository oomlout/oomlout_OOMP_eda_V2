
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Logic_LevelTranslator"
    oIndex = "TXB0108DQSR"
    hexID = "SZKLOGICLEVELTRANSLATORTXB18DQSR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TXB0108DQSR', 'kicadSymbolFootprint': 'Package_SON:USON-20_2x4mm_P0.4mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/txb0108.pdf', 'kicadSymbolki_keywords': 'bidirectional voltage level translator', 'kicadSymbolki_description': '8-bit bidirectional voltage level translator with auto-direction sensing USON package', 'kicadSymbolki_fp_filters': 'USON*2x4mm*P0.4mm*'}])
    newPart['name'].append('Logic_LevelTranslator : TXB0108DQSR')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

