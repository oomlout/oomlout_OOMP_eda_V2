
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Crystal"
    oIndex = "Crystal_SMD_SeikoEpson_FA238V-4Pin_3.2x2.5mm_HandSoldering"
    hexID = "FZKXXSMSEIKOEPSONFA238V4PIN32X25HANDSOLDERING"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Crystal_SMD_SeikoEpson_FA238V-4Pin_3.2x2.5mm_HandSoldering', 'description': 'crystal Epson Toyocom FA-238 series http://www.mouser.com/ds/2/137/1721499-465440.pdf, hand-soldering, 3.2x2.5mm^2 package', 'tags': 'SMD SMT crystal hand-soldering', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Crystal.3dshapes/Crystal_SMD_SeikoEpson_FA238V-4Pin_3.2x2.5mm_HandSoldering.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Crystal : Crystal_SMD_SeikoEpson_FA238V-4Pin_3.2x2.5mm_HandSoldering')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

