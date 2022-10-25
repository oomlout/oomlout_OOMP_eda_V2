
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_USB"
    oIndex = "TUSB7340"
    hexID = "SZKINTERFACEUTU734"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TUSB7340', 'kicadSymbolFootprint': 'Package_DFN_QFN:Texas_S-PWQFN-N100_EP5.5x5.5mm_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/general/docs/lit/getliterature.tsp?genericPartNumber=tusb7320&fileType=pdf', 'kicadSymbolki_keywords': 'USB HUB PCIE', 'kicadSymbolki_description': 'USB 3.0 xHCI Host Controller', 'kicadSymbolki_fp_filters': 'Texas*S?PWQFN?N100*'}])
    newPart['name'].append('Interface_USB : TUSB7340')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

