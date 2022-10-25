
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "FPGA_Microsemi"
    oIndex = "ACT1020PL44"
    hexID = "SZKFPGAMSEMIACT12PL44"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ACT1020PL44', 'kicadSymbolFootprint': 'Package_LCC:PLCC-44_16.6x16.6mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.microsemi.com/document-portal/doc_download/130666-act-1-series-fpgas-datasheet', 'kicadSymbolki_keywords': 'Actel FPGA', 'kicadSymbolki_description': 'ACT1020-PL44, Actel ACT1 FPGA, PLCC-44', 'kicadSymbolki_fp_filters': '*PLCC*16.6x16.6mm*P1.27mm*'}])
    newPart['name'].append('FPGA_Microsemi : ACT1020PL44')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

