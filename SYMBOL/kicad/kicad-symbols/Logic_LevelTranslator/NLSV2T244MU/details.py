
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Logic_LevelTranslator"
    oIndex = "NLSV2T244MU"
    hexID = "SZKLOGICLEVELTRANSLATORNLSV2T244MU"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NLSV2T244MU', 'kicadSymbolFootprint': 'Package_DFN_QFN:OnSemi_UDFN-8_1.2x1.8mm_P0.4mm', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub/Collateral/NLSV2T244-D.PDF', 'kicadSymbolki_keywords': 'Level-Shifter CMOS-TTL-Translation', 'kicadSymbolki_description': 'Dual-Bit Dual-Supply Non-Inverting Level Translator, Output Enable, UDFN-8', 'kicadSymbolki_fp_filters': 'OnSemi*UDFN*1.2x1.8mm*P0.4mm*'}])
    newPart['name'].append('NLSV2T244MU')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

