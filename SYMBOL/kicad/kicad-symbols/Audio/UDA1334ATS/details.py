
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Audio"
    oIndex = "UDA1334ATS"
    hexID = "SZKAUDIOUDA1334ATS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'UDA1334ATS', 'kicadSymbolFootprint': 'Package_SO:SSOP-16_4.4x5.2mm_P0.65mm', 'kicadSymbolDatasheet': 'http://www.nxp.com/docs/en/data-sheet/UDA1334ATS.pdf', 'kicadSymbolki_keywords': 'audio dac 2ch 24bit 96kHz', 'kicadSymbolki_description': 'Low Power Audio DAC with PLL, SSOP-16', 'kicadSymbolki_fp_filters': 'SSOP*4.4x5.2mm*P0.65mm*'}])
    newPart['name'].append('Audio : UDA1334ATS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

