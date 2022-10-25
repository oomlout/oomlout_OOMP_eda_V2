
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IPT015N10N5"
    hexID = "SZKTRANSISTORFETIPT15N1N5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IPT012N08N5', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IPT015N10N5', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:Infineon_PG-HSOF-8-1', 'kicadSymbolDatasheet': 'http://www.infineon.com/dgdl/Infineon-IPT015N10N5-DS-v02_01-EN.pdf?fileId=5546d4624a75e5f1014ac94680661aff', 'kicadSymbolki_keywords': 'OptiMOS Power MOSFET N-MOS', 'kicadSymbolki_description': '300A Id, 100V Vds, OptiMOS N-Channel Power MOSFET, 1.5mOhm Ron, Qg (typ) 169.0nC, PG-HSOF-8', 'kicadSymbolki_fp_filters': 'Infineon*PG*HSOF*'}])
    newPart['name'].append('Transistor_FET : IPT015N10N5')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

