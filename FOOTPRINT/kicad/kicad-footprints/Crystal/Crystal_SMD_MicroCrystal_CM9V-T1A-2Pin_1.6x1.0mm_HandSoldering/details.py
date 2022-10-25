
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Crystal"
    oIndex = "Crystal_SMD_MicroCrystal_CM9V-T1A-2Pin_1.6x1.0mm_HandSoldering"
    hexID = "FZKXXSMMXCM9VT1A2PIN16X1HANDSOLDERING"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Crystal_SMD_MicroCrystal_CM9V-T1A-2Pin_1.6x1.0mm_HandSoldering', 'description': 'SMD Crystal MicroCrystal CM9V-T1A series http://www.microcrystal.com/images/_Product-Documentation/01_TF_ceramic_Packages/01_Datasheet/CM9V-T1A.pdf, hand-soldering, 1.6x1.0mm^2 package', 'tags': 'SMD SMT crystal hand-soldering', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Crystal.3dshapes/Crystal_SMD_MicroCrystal_CM9V-T1A-2Pin_1.6x1.0mm_HandSoldering.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Crystal : Crystal_SMD_MicroCrystal_CM9V-T1A-2Pin_1.6x1.0mm_HandSoldering')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

