
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_STC"
    oIndex = "STC15W201S-35x-SOP16"
    hexID = "SZKMCUSTCSTC15W21S35XS16"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STC15W201S-35x-SOP16', 'kicadSymbolFootprint': 'Package_SO:STC_SOP-16_3.9x9.9mm_P1.27mm', 'kicadSymbolDatasheet': 'www.stcmicro.com/datasheet/STC15F2K60S2-en.pdf', 'kicadSymbolki_keywords': 'STC 8051 microcontroller', 'kicadSymbolki_description': 'Single Chip MCU based on the 8051 architecture, 1KB Flash, 4KB EEPROM, SOP-16', 'kicadSymbolki_fp_filters': 'STC?SOP*3.9x9.9mm*P1.27mm*'}])
    newPart['name'].append('STC15W201S-35x-SOP16')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

