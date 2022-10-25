
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "FPGA_Microsemi"
    oIndex = "EX128-TQ64"
    hexID = "SZKFPGAMSEMIEX128TQ64"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'EX128-TQ64', 'kicadSymbolFootprint': 'Package_QFP:TQFP-64_10x10mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.microsemi.com/document-portal/doc_download/130687-ex-datasheet', 'kicadSymbolki_keywords': 'Actel FPGA eX eX128', 'kicadSymbolki_description': 'Actel eX Family FPGA, 64pin QFP', 'kicadSymbolki_fp_filters': '*TQFP*10x10mm*P0.5mm*'}])
    newPart['name'].append('FPGA_Microsemi : EX128-TQ64')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

