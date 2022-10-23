
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Crystal"
    oIndex = "Crystal_SMD_Abracon_ABM3-2Pin_5.0x3.2mm_HandSoldering"
    hexID = "FZKXXSMABRACONABM32PIN5X32HANDSOLDERING"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Crystal_SMD_Abracon_ABM3-2Pin_5.0x3.2mm_HandSoldering', 'description': 'Abracon Miniature Ceramic Smd Crystal ABM3 http://www.abracon.com/Resonators/abm3.pdf, hand-soldering, 5.0x3.2mm^2 package', 'tags': 'SMD SMT crystal hand-soldering', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Crystal.3dshapes/Crystal_SMD_Abracon_ABM3-2Pin_5.0x3.2mm_HandSoldering.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Crystal : Crystal_SMD_Abracon_ABM3-2Pin_5.0x3.2mm_HandSoldering')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

