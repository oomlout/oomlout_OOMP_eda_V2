
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_SAMA"
    oIndex = "ATSAMA5D21"
    hexID = "SZKMCUMCHIPSAMAATSAMA5D21"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATSAMA5D21', 'kicadSymbolFootprint': 'Package_BGA:Microchip_TFBGA-196_11x11mm_Layout14x14_P0.75mm_SMD', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/SAMA5D2-Series-Data-Sheet-DS60001476C.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'MPU Cortex-A5 Cortex A5 Linux DDR DRAM BGA', 'kicadSymbolki_description': 'ARM Cortex-A5 MPU, 500 MHz max, 1x SDIO/SD-CARD/eMMC/QSPI memory, 128 kB SRAM, 16-bit bus DDR2/DDR3 RAM, 1.1-1.32 V, 72 GPIO, TFBGA-196', 'kicadSymbolki_fp_filters': 'Microchip*TFBGA*11x11mm*P0.75mm*'}])
    newPart['name'].append('ATSAMA5D21')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

