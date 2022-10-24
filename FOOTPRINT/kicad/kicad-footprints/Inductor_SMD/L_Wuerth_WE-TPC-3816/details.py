
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_SMD"
    oIndex = "L_Wuerth_WE-TPC-3816"
    hexID = "FZKINDUCTORSMLWUERTHWETPC3816"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Wuerth_WE-TPC-3816', 'description': 'L_Wuerth_WE-TPC-3816 StepUp generated footprint, http://katalog.we-online.de/pbs/datasheet/7440310047.pdf', 'tags': 'wurth wuerth smd inductor', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_Wuerth_WE-TPC-3816.wrl', 'pins': {'type': 'smd', 'shape': 'custom'}})
    newPart['name'].append('Inductor_SMD : L_Wuerth_WE-TPC-3816')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

