
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Mounting_Wuerth"
    oIndex = "Mounting_Wuerth_WA-SMSSR-3.3mm_H8mm_SnapRivet_9776080960"
    hexID = "FZKMONMONWASMSSR33H8SNAPRIVET9776896"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Mounting_Wuerth_WA-SMSSR-3.3mm_H8mm_SnapRivet_9776080960', 'description': 'Mounting Hardware, inside through hole 3.3mm, height 8, Wuerth electronics 9776080960 (https://katalog.we-online.com/em/datasheet/9776080960.pdf), generated with kicad-footprint-generator', 'tags': 'Mounting 3.3mm 9776080960', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Mounting_Wuerth.3dshapes/Mounting_Wuerth_WA-SMSSR-3.3mm_H8mm_SnapRivet_9776080960.wrl', 'pins': {'type': 'smd', 'shape': 'custom'}})
    newPart['name'].append('Mounting_Wuerth : Mounting_Wuerth_WA-SMSSR-3.3mm_H8mm_SnapRivet_9776080960')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

