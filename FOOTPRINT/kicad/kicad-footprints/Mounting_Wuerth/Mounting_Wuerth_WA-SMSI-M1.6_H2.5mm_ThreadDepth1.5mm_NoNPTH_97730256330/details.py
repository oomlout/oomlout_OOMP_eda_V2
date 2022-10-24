
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Mounting_Wuerth"
    oIndex = "Mounting_Wuerth_WA-SMSI-M1.6_H2.5mm_ThreadDepth1.5mm_NoNPTH_97730256330"
    hexID = "FZKMONMONWASMSIM16H25THREADDEP15NONP977325633"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Mounting_Wuerth_WA-SMSI-M1.6_H2.5mm_ThreadDepth1.5mm_NoNPTH_97730256330', 'description': 'Mounting Hardware, inside blind hole M1.6, height 2.5, Wuerth electronics 97730256330 (https://katalog.we-online.com/em/datasheet/97730256330R.pdf), generated with kicad-footprint-generator', 'tags': 'Mounting M1.6 97730256330', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Mounting_Wuerth.3dshapes/Mounting_Wuerth_WA-SMSI-M1.6_H2.5mm_ThreadDepth1.5mm_NoNPTH_97730256330.wrl', 'pins': {'type': 'smd', 'shape': 'custom'}})
    newPart['name'].append('Mounting_Wuerth : Mounting_Wuerth_WA-SMSI-M1.6_H2.5mm_ThreadDepth1.5mm_NoNPTH_97730256330')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

