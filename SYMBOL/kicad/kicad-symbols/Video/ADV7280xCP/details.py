
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Video"
    oIndex = "ADV7280xCP"
    hexID = "SZKVIDEOADV728XCP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADV7280xCP', 'kicadSymbolFootprint': 'Package_CSP:LFCSP-32-1EP_5x5mm_P0.5mm_EP3.6x3.6mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/ADV7280.PDF', 'kicadSymbolki_keywords': 'video decoder', 'kicadSymbolki_description': '10-Bit, 4x Oversampled SDTV Video Decoder with Deinterlacer, LFCSP-32', 'kicadSymbolki_fp_filters': 'LFCSP*1EP*5x5mm*P0.5mm*'}])
    newPart['name'].append('Video : ADV7280xCP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

