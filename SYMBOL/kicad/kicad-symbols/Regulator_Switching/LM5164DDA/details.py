
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LM5164DDA"
    hexID = "SZKREGULATORSWITCHINGLM5164DDA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM5164DDA', 'kicadSymbolFootprint': 'Package_SO:HSOP-8-1EP_3.9x4.9mm_P1.27mm_EP2.41x3.1mm_ThermalVias', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/lm5164.pdf?ts=1598311864250&ref_url=https%253A%252F%252Fwww.ti.com%252Fproduct%252FLM5164%253FHQS%253DTI-null-null-octopart-df-pf-null-wwe', 'kicadSymbolki_keywords': 'step-down dc-dc buck regulator adjustable', 'kicadSymbolki_description': '1A synchronous buck converter with ultra-low IQ, 6V - 100V input, adjustable output voltage, HSOP-8', 'kicadSymbolki_fp_filters': 'HSOP*1EP*3.9x4.9*P1.27mm*'}])
    newPart['name'].append('Regulator_Switching : LM5164DDA')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

