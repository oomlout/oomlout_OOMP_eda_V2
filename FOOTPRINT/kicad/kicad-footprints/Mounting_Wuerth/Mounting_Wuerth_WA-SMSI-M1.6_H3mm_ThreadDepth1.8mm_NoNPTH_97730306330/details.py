
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Mounting_Wuerth"
    oIndex = "Mounting_Wuerth_WA-SMSI-M1.6_H3mm_ThreadDepth1.8mm_NoNPTH_97730306330"
    hexID = "FZKMONMONWASMSIM16H3THREADDEP18NONP97733633"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Mounting_Wuerth_WA-SMSI-M1.6_H3mm_ThreadDepth1.8mm_NoNPTH_97730306330', 'description': 'Mounting Hardware, inside blind hole M1.6, height 3, Wuerth electronics 97730306330 (https://katalog.we-online.com/em/datasheet/97730306330.pdf), generated with kicad-footprint-generator', 'tags': 'Mounting M1.6 97730306330', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Mounting_Wuerth.3dshapes/Mounting_Wuerth_WA-SMSI-M1.6_H3mm_ThreadDepth1.8mm_NoNPTH_97730306330.wrl', 'pins': {'type': 'smd', 'shape': 'custom'}})
    newPart['name'].append('Mounting_Wuerth : Mounting_Wuerth_WA-SMSI-M1.6_H3mm_ThreadDepth1.8mm_NoNPTH_97730306330')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

