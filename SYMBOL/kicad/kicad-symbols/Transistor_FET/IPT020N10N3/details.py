
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IPT020N10N3"
    hexID = "SZKTRANSISTORFETIPT2N1N3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IPT012N08N5', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IPT020N10N3', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:Infineon_PG-HSOF-8-1', 'kicadSymbolDatasheet': 'http://www.infineon.com/dgdl/Infineon-IPT020N10N3-DS-v02_00-en.pdf?fileId=db3a30433e9d5d11013e9e58035b0158', 'kicadSymbolki_keywords': 'OptiMOS Power MOSFET N-MOS', 'kicadSymbolki_description': '300A Id, 100V Vds, OptiMOS N-Channel Power MOSFET, 2.0mOhm Ron, Qg (typ) 156.0nC, PG-HSOF-8', 'kicadSymbolki_fp_filters': 'Infineon*PG*HSOF*'}])
    newPart['name'].append('Transistor_FET : IPT020N10N3')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

