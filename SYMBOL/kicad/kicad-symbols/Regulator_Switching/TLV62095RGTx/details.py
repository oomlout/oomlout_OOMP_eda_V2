
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "TLV62095RGTx"
    hexID = "SZKREGULATORSWITCHINGTLV6295RGTX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TLV62095RGTx', 'kicadSymbolFootprint': 'Package_DFN_QFN:VQFN-16-1EP_3x3mm_P0.5mm_EP1.68x1.68mm_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tlv62095.pdf', 'kicadSymbolki_keywords': 'Synchronous Buck', 'kicadSymbolki_description': 'High efficiency step-down converter', 'kicadSymbolki_fp_filters': 'VQFN*1EP*3x3mm*P0.5mm*'}])
    newPart['name'].append('Regulator_Switching : TLV62095RGTx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

