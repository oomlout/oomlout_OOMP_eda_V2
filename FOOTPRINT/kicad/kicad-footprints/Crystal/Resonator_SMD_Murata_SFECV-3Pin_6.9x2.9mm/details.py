
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Crystal"
    oIndex = "Resonator_SMD_Murata_SFECV-3Pin_6.9x2.9mm"
    hexID = "FZKXRSSFECV3PIN69X29"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Resonator_SMD_Murata_SFECV-3Pin_6.9x2.9mm', 'description': 'SMD Resomator/Filter Murata SFECV, http://cdn-reichelt.de/documents/datenblatt/B400/SFECV-107.pdf, 6.9x2.9mm^2 package', 'tags': 'SMD SMT ceramic resonator filter filter', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Crystal.3dshapes/Resonator_SMD_Murata_SFECV-3Pin_6.9x2.9mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Crystal : Resonator_SMD_Murata_SFECV-3Pin_6.9x2.9mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

