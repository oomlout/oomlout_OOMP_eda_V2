
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Mounting_Wuerth"
    oIndex = "Mounting_Wuerth_WA-SMSI-M1.6_H3.5mm_ThreadDepth2mm_97730356332"
    hexID = "FZKMONMONWASMSIM16H35THREADDEP29773356332"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Mounting_Wuerth_WA-SMSI-M1.6_H3.5mm_ThreadDepth2mm_97730356332', 'description': 'Mounting Hardware, inside blind hole M1.6, height 3.5, Wuerth electronics 97730356332 (https://katalog.we-online.com/em/datasheet/97730356332.pdf), generated with kicad-footprint-generator', 'tags': 'Mounting M1.6 97730356332', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Mounting_Wuerth.3dshapes/Mounting_Wuerth_WA-SMSI-M1.6_H3.5mm_ThreadDepth2mm_97730356332.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Mounting_Wuerth : Mounting_Wuerth_WA-SMSI-M1.6_H3.5mm_ThreadDepth2mm_97730356332')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

