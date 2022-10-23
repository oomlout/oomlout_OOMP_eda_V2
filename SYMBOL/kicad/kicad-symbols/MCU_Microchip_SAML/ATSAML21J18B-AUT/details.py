
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_SAML"
    oIndex = "ATSAML21J18B-AUT"
    hexID = "SZKMCUMCHIPSAMLATSAML21J18BAUT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ATSAML21J16B-AUT', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATSAML21J18B-AUT', 'kicadSymbolFootprint': 'Package_QFP:TQFP-64_10x10mm_P0.5mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/60001477A.pdf', 'kicadSymbolki_keywords': '32-bit ARM Cortex-M0+ MCU Microcontroller', 'kicadSymbolki_description': 'SAM L21 Microchip SMART ARM-based Flash MCU, 48Mhz, 256K Flash, 32K SRAM, TQFP64', 'kicadSymbolki_fp_filters': 'TQFP*64*10x10mm*P0.5mm*'}])
    newPart['name'].append('ATSAML21J18B-AUT')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

