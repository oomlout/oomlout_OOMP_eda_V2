
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_ATmega"
    oIndex = "ATmega169PV-8MC"
    hexID = "SZKMCUMCHIPATMEGAATMEGA169PV8MC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATmega169PV-8MC', 'kicadSymbolFootprint': 'Package_DFN_QFN:Microchip_DRQFN-64-1EP_7x7mm_P0.65mm_EP4.1x4.1mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/doc8018.pdf', 'kicadSymbolki_keywords': 'AVR 8bit Microcontroller MegaAVR LCD PicoPower', 'kicadSymbolki_description': '8MHz, 16kB Flash, 1kB SRAM, 512B EEPROM, DRQFN-64', 'kicadSymbolki_fp_filters': 'Microchip*DRQFN*1EP*7x7mm*P0.65mm*'}])
    newPart['name'].append('ATmega169PV-8MC')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

