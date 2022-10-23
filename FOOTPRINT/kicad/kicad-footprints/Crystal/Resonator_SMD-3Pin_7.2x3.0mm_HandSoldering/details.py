
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Crystal"
    oIndex = "Resonator_SMD-3Pin_7.2x3.0mm_HandSoldering"
    hexID = "FZKXRSM3PIN72X3HANDSOLDERING"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Resonator_SMD-3Pin_7.2x3.0mm_HandSoldering', 'description': 'SMD Resomator/Filter 7.2x3.0mm, Murata CSTCC8M00G53-R0; 8MHz resonator, SMD, Farnell (Element 14) #1170435, http://www.farnell.com/datasheets/19296.pdf?_ga=1.247244932.122297557.1475167906, hand-soldering, 7.2x3.0mm^2 package', 'tags': 'SMD SMT ceramic resonator filter filter hand-soldering', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Crystal.3dshapes/Resonator_SMD-3Pin_7.2x3.0mm_HandSoldering.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Crystal : Resonator_SMD-3Pin_7.2x3.0mm_HandSoldering')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

