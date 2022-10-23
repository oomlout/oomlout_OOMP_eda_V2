
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "FSDH321L"
    hexID = "SZKREGULATORSWITCHINGFSDH321L"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'FSDH321L', 'kicadSymbolFootprint': 'Package_DIP:Fairchild_LSOP-8', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/FSDH321JP-D.pdf', 'kicadSymbolki_keywords': 'SMPS Controller with MOSFET 17W AC-DC', 'kicadSymbolki_description': '17W SMPS Controller, 100kHz, AC-DC, SMD-8', 'kicadSymbolki_fp_filters': 'Fairchild*LSOP*'}])
    newPart['name'].append('FSDH321L')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

