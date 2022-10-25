
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Controller"
    oIndex = "NCP4308DMT"
    hexID = "SZKREGULATORCONTROLLERNCP438DMT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'NCP4308AMT', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NCP4308DMT', 'kicadSymbolFootprint': 'Package_DFN_QFN:OnSemi_DFN-8_2x2mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub/Collateral/NCP4308-D.PDF', 'kicadSymbolki_keywords': 'synchronous rectifier controller', 'kicadSymbolki_description': 'Synchronous Rectifier Controller, 4A/8A, 4V UVLO, WDFN-8', 'kicadSymbolki_fp_filters': 'OnSemi*DFN*2x2mm*P0.5mm*'}])
    newPart['name'].append('Regulator_Controller : NCP4308DMT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

