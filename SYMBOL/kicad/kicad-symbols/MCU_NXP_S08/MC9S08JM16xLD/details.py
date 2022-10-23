
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_S08"
    oIndex = "MC9S08JM16xLD"
    hexID = "SZKMCUNXPS8MC9S8JM16XLD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MC9S08JM60xLD', 'kicadSymbolReference': 'IC', 'kicadSymbolValue': 'MC9S08JM16xLD', 'kicadSymbolFootprint': 'Package_QFP:LQFP-44_10x10mm_P0.8mm', 'kicadSymbolDatasheet': 'http://cache.nxp.com/files/microcontrollers/doc/data_sheet/MC9S08JM16.pdf', 'kicadSymbolki_keywords': 'NXP S08 Microcontroller', 'kicadSymbolki_description': '8-bit USB Cost-Effective Microcontroller, S08 core, 16kB Flash, 1kB RAM, LQFP-44', 'kicadSymbolki_fp_filters': 'LQFP*10x10mm*P0.8mm*'}])
    newPart['name'].append('MC9S08JM16xLD')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

