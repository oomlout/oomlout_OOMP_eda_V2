
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "NCP115AMX250TCG"
    hexID = "SZKREGULATORLINEARNCP115AMX25TCG"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'NCP115AMX120TCG', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NCP115AMX250TCG', 'kicadSymbolFootprint': 'Package_DFN_QFN:OnSemi_XDFN4-1EP_1.0x1.0mm_EP0.52x0.52mm', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/NCP115-D.PDF', 'kicadSymbolki_keywords': 'Single Output LDO', 'kicadSymbolki_description': '300mA Low-Dropout Linear Regulators, 2.5V output voltage, LDO with low noise and enable pin, XDFN-4', 'kicadSymbolki_fp_filters': 'OnSemi*XDFN4*1EP*1.0x1.0mm*'}])
    newPart['name'].append('Regulator_Linear : NCP115AMX250TCG')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

