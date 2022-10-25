
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Logic_LevelTranslator"
    oIndex = "FXMA108"
    hexID = "SZKLOGICLEVELTRANSLATORFXMA18"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'FXMA108', 'kicadSymbolFootprint': 'Package_DFN_QFN:WQFN-20-1EP_2.5x4.5mm_P0.5mm_EP1x2.9mm', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub/Collateral/FXMA108-D.pdf', 'kicadSymbolki_keywords': 'Level shifter translator bidirectional', 'kicadSymbolki_description': 'Dual-Supply, 8-Bit Signal Translator with Configurable Voltage Supplies and Signals Levels, 3-State Outputs and Auto Direction Sensing, WQFN-20', 'kicadSymbolki_fp_filters': 'WQFN*2.5x4.5mm*P0.5mm*EP1x2.9mm*'}])
    newPart['name'].append('Logic_LevelTranslator : FXMA108')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

