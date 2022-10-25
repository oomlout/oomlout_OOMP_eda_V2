
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_S08"
    oIndex = "MC9S08JS8CWJ"
    hexID = "SZKMCUNXPS8MC9S8JS8CWJ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MC9S08JS16CWJ', 'kicadSymbolReference': 'IC', 'kicadSymbolValue': 'MC9S08JS8CWJ', 'kicadSymbolFootprint': 'Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm', 'kicadSymbolDatasheet': 'http://cache.nxp.com/files/32bit/doc/ref_manual/MC9S08JS16RM.pdf', 'kicadSymbolki_keywords': 'NXP S08 Microcontroller', 'kicadSymbolki_description': '8-bit USB Microcontroller, S08 core, 8kB Flash, 512B RAM, SOIC-20', 'kicadSymbolki_fp_filters': 'SOIC*7.5x12.8mm*P1.27mm*'}])
    newPart['name'].append('MCU_NXP_S08 : MC9S08JS8CWJ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

