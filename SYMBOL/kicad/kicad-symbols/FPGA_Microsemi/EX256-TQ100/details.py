
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "FPGA_Microsemi"
    oIndex = "EX256-TQ100"
    hexID = "SZKFPGAMSEMIEX256TQ1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'EX256-TQ100', 'kicadSymbolFootprint': 'Package_QFP:TQFP-100_14x14mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.microsemi.com/document-portal/doc_download/130687-ex-datasheet', 'kicadSymbolki_keywords': 'Actel FPGA eX eX256', 'kicadSymbolki_description': 'Actel eX FPGA Family, 100pin QFP', 'kicadSymbolki_fp_filters': '*QFP*14x14mm*P0.5mm*'}])
    newPart['name'].append('FPGA_Microsemi : EX256-TQ100')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

