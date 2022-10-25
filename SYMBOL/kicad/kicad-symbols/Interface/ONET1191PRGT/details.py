
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface"
    oIndex = "ONET1191PRGT"
    hexID = "SZKINTERFACEONET1191PRGT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ONET1191PRGT', 'kicadSymbolFootprint': 'Package_DFN_QFN:VQFN-16-1EP_3x3mm_P0.5mm_EP1.68x1.68mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/onet1191p.pdf', 'kicadSymbolki_keywords': 'limiting amplifier gigabit ethernet sfp sfp+', 'kicadSymbolki_description': '11.3-Gbps Limiting Amplifier, VQFN-16', 'kicadSymbolki_fp_filters': 'VQFN*1EP*3x3mm*P0.5mm*'}])
    newPart['name'].append('Interface : ONET1191PRGT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

