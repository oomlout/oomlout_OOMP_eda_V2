
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Crystal"
    oIndex = "Crystal_SMD_SeikoEpson_MC306-4Pin_8.0x3.2mm_HandSoldering"
    hexID = "FZKXXSMSEIKOEPSONMC364PIN8X32HANDSOLDERING"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Crystal_SMD_SeikoEpson_MC306-4Pin_8.0x3.2mm_HandSoldering', 'description': 'SMD Crystal Seiko Epson MC-306 https://support.epson.biz/td/api/doc_check.php?dl=brief_MC-306_en.pdf, hand-soldering, 8.0x3.2mm^2 package', 'tags': 'SMD SMT crystal hand-soldering', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Crystal.3dshapes/Crystal_SMD_SeikoEpson_MC306-4Pin_8.0x3.2mm_HandSoldering.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Crystal : Crystal_SMD_SeikoEpson_MC306-4Pin_8.0x3.2mm_HandSoldering')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

