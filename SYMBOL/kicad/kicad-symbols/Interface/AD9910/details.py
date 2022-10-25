
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface"
    oIndex = "AD9910"
    hexID = "SZKINTERFACEAD991"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD9910', 'kicadSymbolFootprint': 'Package_QFP:TQFP-100-1EP_14x14mm_P0.5mm_EP5x5mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/AD9910.pdf', 'kicadSymbolki_keywords': 'dds direct digital synthesizer', 'kicadSymbolki_description': '1 GSPS, 14-Bit, 3.3V CMOS, Direct Digital Synthesizer, QFP-100', 'kicadSymbolki_fp_filters': 'TQFP*14x14mm*P0.5mm*EP5x5mm*'}])
    newPart['name'].append('Interface : AD9910')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

