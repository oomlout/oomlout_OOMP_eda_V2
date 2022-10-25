
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LP38512MR-ADJ"
    hexID = "SZKREGULATORLINEARLP38512MRADJ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LP38512MR-ADJ', 'kicadSymbolFootprint': 'Package_SO:Texas_HTSOP-8-1EP_3.9x4.9mm_P1.27mm_EP2.95x4.9mm_Mask2.4x3.1mm_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lp38512-adj.pdf', 'kicadSymbolki_keywords': 'LDO Linear Regulator', 'kicadSymbolki_description': '1.5A Fast-Transient Response Low-Dropout Linear Voltage Regulator with Error Flag, Adjustable Output, HTSOP-8', 'kicadSymbolki_fp_filters': 'Texas*HTSOP*1EP*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Regulator_Linear : LP38512MR-ADJ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

