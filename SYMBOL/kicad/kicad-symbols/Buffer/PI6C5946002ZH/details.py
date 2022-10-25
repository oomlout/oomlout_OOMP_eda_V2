
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Buffer"
    oIndex = "PI6C5946002ZH"
    hexID = "SZKBUFFERPI6C59462ZH"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PI6C5946002ZH', 'kicadSymbolFootprint': 'Package_DFN_QFN:TQFN-16-1EP_3x3mm_P0.5mm_EP1.6x1.6mm', 'kicadSymbolDatasheet': 'https://www.diodes.com/assets/Datasheets/PI6C5946002.pdf', 'kicadSymbolki_keywords': 'buffer clock data', 'kicadSymbolki_description': '6 GHz / 12 Gbps Clock / Data 1:2 Fanout Buffer with Internal Termination, TQFN-16', 'kicadSymbolki_fp_filters': 'TQFN*1EP*3x3mm*P0.5mm*'}])
    newPart['name'].append('Buffer : PI6C5946002ZH')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

