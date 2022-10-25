
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_S08"
    oIndex = "MC9S08QA2CDNE"
    hexID = "SZKMCUNXPS8MC9S8QA2CDNE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MC9S08QA4CDNE', 'kicadSymbolReference': 'IC', 'kicadSymbolValue': 'MC9S08QA2CDNE', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'http://cache.nxp.com/files/microcontrollers/doc/ref_manual/MC9S08QA4RM.pdf', 'kicadSymbolki_keywords': 'NXP S08 Microcontroller', 'kicadSymbolki_description': '8-bit Small Package Microcontroller, S08 core, 2kB Flash, 160B RAM, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('MCU_NXP_S08 : MC9S08QA2CDNE')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

