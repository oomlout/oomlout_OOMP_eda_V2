
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Timer_RTC"
    oIndex = "AB1815"
    hexID = "SZKTIMERRTCAB1815"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AB1815', 'kicadSymbolFootprint': 'Package_DFN_QFN:VQFN-16-1EP_3x3mm_P0.5mm_EP1.8x1.8mm', 'kicadSymbolDatasheet': 'https://abracon.com/Precisiontiming/AB18X5-RTC.pdf', 'kicadSymbolki_keywords': 'rtc', 'kicadSymbolki_description': 'Real-Time Clock, SPI Interface, 3 GPO, QFN-16', 'kicadSymbolki_fp_filters': 'VQFN*1EP*3x3mm*P0.5mm*'}])
    newPart['name'].append('Timer_RTC : AB1815')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

