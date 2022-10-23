
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Crystal"
    oIndex = "Resonator_SMD_Murata_TPSKA-3Pin_7.9x3.8mm"
    hexID = "FZKXRSTPSKA3PIN79X38"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Resonator_SMD_Murata_TPSKA-3Pin_7.9x3.8mm', 'description': 'SMD Resomator/Filter Murata TPSKA, http://cdn-reichelt.de/documents/datenblatt/B400/SFECV-107.pdf, 7.9x3.8mm^2 package', 'tags': 'SMD SMT ceramic resonator filter filter', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Crystal.3dshapes/Resonator_SMD_Murata_TPSKA-3Pin_7.9x3.8mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Crystal : Resonator_SMD_Murata_TPSKA-3Pin_7.9x3.8mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

