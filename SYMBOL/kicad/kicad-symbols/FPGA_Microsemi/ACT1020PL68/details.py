
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "FPGA_Microsemi"
    oIndex = "ACT1020PL68"
    hexID = "SZKFPGAMSEMIACT12PL68"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ACT1020PL68', 'kicadSymbolFootprint': 'Package_LCC:PLCC-68_24.2x24.2mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.microsemi.com/document-portal/doc_download/130666-act-1-series-fpgas-datasheet', 'kicadSymbolki_keywords': 'Actel FPGA', 'kicadSymbolki_description': 'ACT1020-PL68, Actel ACT1 FPGA, PLCC-68', 'kicadSymbolki_fp_filters': '*PLCC*24.2x24.2mm*P1.27mm*'}])
    newPart['name'].append('ACT1020PL68')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

