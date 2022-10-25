
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "TPS54560BDDA"
    hexID = "SZKREGULATORSWITCHINGTPS5456BDDA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS54560BDDA', 'kicadSymbolFootprint': 'Package_SO:Texas_R-PDSO-G8_EP2.95x4.9mm_Mask2.4x3.1mm_ThermalVias', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/tps54560b.pdf', 'kicadSymbolki_keywords': 'buck controller', 'kicadSymbolki_description': '5A, Step Down DC-DC Converter, 4.5-60V Input Voltage, Texas R-PDSO-G8', 'kicadSymbolki_fp_filters': 'Texas*R*PDSO*G8*'}])
    newPart['name'].append('Regulator_Switching : TPS54560BDDA')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

