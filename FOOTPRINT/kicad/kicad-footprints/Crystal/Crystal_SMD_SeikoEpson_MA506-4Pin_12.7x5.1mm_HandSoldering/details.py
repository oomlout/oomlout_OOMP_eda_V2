
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Crystal"
    oIndex = "Crystal_SMD_SeikoEpson_MA506-4Pin_12.7x5.1mm_HandSoldering"
    hexID = "FZKXXSMSEIKOEPSONMA564PIN127X51HANDSOLDERING"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Crystal_SMD_SeikoEpson_MA506-4Pin_12.7x5.1mm_HandSoldering', 'description': 'SMD Crystal Seiko Epson MC-506 http://media.digikey.com/pdf/Data%20Sheets/Epson%20PDFs/MA-505,506.pdf, hand-soldering, 12.7x5.1mm^2 package', 'tags': 'SMD SMT crystal hand-soldering', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Crystal.3dshapes/Crystal_SMD_SeikoEpson_MA506-4Pin_12.7x5.1mm_HandSoldering.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Crystal : Crystal_SMD_SeikoEpson_MA506-4Pin_12.7x5.1mm_HandSoldering')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

