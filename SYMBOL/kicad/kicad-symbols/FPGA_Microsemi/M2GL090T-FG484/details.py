
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "FPGA_Microsemi"
    oIndex = "M2GL090T-FG484"
    hexID = "SZKFPGAMSEMIM2GL9TFG484"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'M2GL090T-FG484', 'kicadSymbolFootprint': 'Package_BGA:BGA-484_23.0x23.0mm_Layout22x22_P1.0mm', 'kicadSymbolDatasheet': 'https://www.microsemi.com/document-portal/doc_download/132042-ds0128-igloo2-and-smartfusion2-datasheet', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'FPGA Igloo2 BGA', 'kicadSymbolki_description': ' IGLOO2 FPGA and SmartFusion2 SoC FPGA', 'kicadSymbolki_fp_filters': 'BGA*484*23.0x23.0mm*Layout22x22*P1.0mm*'}])
    newPart['name'].append('M2GL090T-FG484')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

