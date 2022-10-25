
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_ATmega"
    oIndex = "ATmega169PA-MC"
    hexID = "SZKMCUMCHIPATMEGAATMEGA169PAMC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ATmega169PV-8MC', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATmega169PA-MC', 'kicadSymbolFootprint': 'Package_DFN_QFN:Microchip_DRQFN-64-1EP_7x7mm_P0.65mm_EP4.1x4.1mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/atmel-8284-8-bit-avr-microcontroller-atmega169a_pa_329a_pa_3290a_pa_649a_p_6490a_p_datasheet.pdf', 'kicadSymbolki_keywords': 'AVR 8bit Microcontroller MegaAVR LCD PicoPower', 'kicadSymbolki_description': '16MHz, 16kB Flash, 1kB SRAM, 512B EEPROM, DRQFN-64', 'kicadSymbolki_fp_filters': 'Microchip*DRQFN*1EP*7x7mm*P0.65mm*'}])
    newPart['name'].append('MCU_Microchip_ATmega : ATmega169PA-MC')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

