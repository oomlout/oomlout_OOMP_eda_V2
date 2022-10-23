
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_Kinetis"
    oIndex = "MKE02Z32VLH4"
    hexID = "SZKMCUNXPKINETISMKE2Z32VLH4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MKE02Z64VLH4', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MKE02Z32VLH4', 'kicadSymbolFootprint': 'Package_QFP:LQFP-64_10x10mm_P0.5mm', 'kicadSymbolDatasheet': 'http://cache.nxp.com/files/microcontrollers/doc/ref_manual/MKE02P64M40SF0RM.pdf', 'kicadSymbolki_keywords': 'NXP Kinetis Microcontroller', 'kicadSymbolki_description': '40 MHz, Entry-Level, High-Robustness, ESD/EMC performance Microcontroller, Cortex-M0+ core, 32kB Flash, 4kB RAM, LQFP-64', 'kicadSymbolki_fp_filters': 'LQFP*10x10mm*P0.5mm*'}])
    newPart['name'].append('MKE02Z32VLH4')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

