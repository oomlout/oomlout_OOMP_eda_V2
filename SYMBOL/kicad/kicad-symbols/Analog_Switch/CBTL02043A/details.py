
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_Switch"
    oIndex = "CBTL02043A"
    hexID = "SZKANALOGSWITCHCBTL243A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CBTL02043A', 'kicadSymbolFootprint': 'Package_DFN_QFN:WQFN-20-1EP_2.5x4.5mm_P0.5mm_EP1x2.9mm', 'kicadSymbolDatasheet': 'https://www.nxp.com/docs/en/data-sheet/CBTL02043A_CBTL02043B.pdf', 'kicadSymbolki_keywords': 'Multiplexer Demultiplexer Switch Hi-Speed', 'kicadSymbolki_description': '3.3 V, 2 differential channel, 2:1 MUX/deMUX switch, 10 Gbps, WQFN-20', 'kicadSymbolki_fp_filters': 'WQFN*1EP*2.5x4.5mm*P0.5mm*'}])
    newPart['name'].append('CBTL02043A')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

