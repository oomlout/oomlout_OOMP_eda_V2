
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_SMD"
    oIndex = "L_Wuerth_WE-PDF_Handsoldering"
    hexID = "FZKINDUCTORSMLWUERTHWEPDFHANDSOLDERING"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Wuerth_WE-PDF_Handsoldering', 'description': 'Shielded Power Inductor, Wuerth Elektronik, WE-PDF, SMD, Handsoldering, https://katalog.we-online.de/pbs/datasheet/7447797022.pdf', 'tags': 'Choke Shielded Power Inductor WE-PDF Wuerth Handsoldering', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_Wuerth_WE-PDF.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Inductor_SMD : L_Wuerth_WE-PDF_Handsoldering')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

