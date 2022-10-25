
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "TSV911IDT"
    hexID = "SZKAMPLIFIEROPERATIONALTSV911IDT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'OPA333xxD', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TSV911IDT', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'www.st.com/resource/en/datasheet/tsv911.pdf', 'kicadSymbolki_keywords': 'single opamp', 'kicadSymbolki_description': 'Single rail-to-rail input/output 8 MHz operational amplifiers, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Amplifier_Operational : TSV911IDT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

