
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_Relay"
    oIndex = "TPL9201_TSSOP"
    hexID = "SZKDRIVERRELAYTPL921TSS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPL9201_TSSOP', 'kicadSymbolFootprint': 'Package_SO:HTSSOP-20-1EP_4.4x6.5mm_P0.65mm_EP3.4x6.5mm_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tpl9201.pdf', 'kicadSymbolki_keywords': 'Relay Driver', 'kicadSymbolki_description': '8-CHANNEL RELAY DRIVER WITH INTEGRATED 5-V LDO AND ZERO-VOLT DETECTION TSSOP-20', 'kicadSymbolki_fp_filters': 'HTSSOP*4.4x6.5mm*P0.65mm*ThermalVias*'}])
    newPart['name'].append('Driver_Relay : TPL9201_TSSOP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

