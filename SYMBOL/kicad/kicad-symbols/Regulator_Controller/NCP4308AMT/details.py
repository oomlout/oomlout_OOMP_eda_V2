
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Controller"
    oIndex = "NCP4308AMT"
    hexID = "SZKREGULATORCONTROLLERNCP438AMT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NCP4308AMT', 'kicadSymbolFootprint': 'Package_DFN_QFN:OnSemi_DFN-8_2x2mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub/Collateral/NCP4308-D.PDF', 'kicadSymbolki_keywords': 'synchronous rectifier controller', 'kicadSymbolki_description': 'Synchronous Rectifier Controller, 4A/8A, 4V UVLO, GaN Capable, WDFN-8', 'kicadSymbolki_fp_filters': 'OnSemi*DFN*2x2mm*P0.5mm*'}])
    newPart['name'].append('NCP4308AMT')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

