
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "FSDL321L"
    hexID = "SZKREGULATORSWITCHINGFSDL321L"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'FSDH321L', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'FSDL321L', 'kicadSymbolFootprint': 'Package_DIP:Fairchild_LSOP-8', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/FSDH321JP-D.pdf', 'kicadSymbolki_keywords': 'SMPS Controller with MOSFET 17W AC-DC', 'kicadSymbolki_description': '17W SMPS Controller, 50kHz, AC-DC, SMD-8', 'kicadSymbolki_fp_filters': 'Fairchild*LSOP*'}])
    newPart['name'].append('FSDL321L')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

