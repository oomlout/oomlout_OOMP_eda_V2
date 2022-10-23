
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "FPGA_Microsemi"
    oIndex = "A3P060-VQG100"
    hexID = "SZKFPGAMSEMIA3P6VQG1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'A3P060-VQG100', 'kicadSymbolFootprint': 'Package_QFP:VQFP-100_14x14mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.microsemi.com/document-portal/doc_download/130704-proasic3-flash-family-fpgas-datasheet', 'kicadSymbolki_keywords': 'ProASIC3 ACTEL FLASH', 'kicadSymbolki_description': 'Actel ProASIC3 Flash Family FPGAs, 512 MCLB, 100pin QFP100', 'kicadSymbolki_fp_filters': '*QFP*14x14mm*P0.5mm*'}])
    newPart['name'].append('A3P060-VQG100')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

