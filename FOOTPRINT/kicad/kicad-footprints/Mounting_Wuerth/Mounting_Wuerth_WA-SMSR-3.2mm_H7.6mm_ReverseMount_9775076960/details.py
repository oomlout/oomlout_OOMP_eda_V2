
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Mounting_Wuerth"
    oIndex = "Mounting_Wuerth_WA-SMSR-3.2mm_H7.6mm_ReverseMount_9775076960"
    hexID = "FZKMONMONWASMSR32H76RMOUNT97757696"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Mounting_Wuerth_WA-SMSR-3.2mm_H7.6mm_ReverseMount_9775076960', 'description': 'Mounting Hardware, inside through hole 3.2mm, height 7.6, Wuerth electronics 9775076960 (https://katalog.we-online.com/em/datasheet/9775076960.pdf), generated with kicad-footprint-generator', 'tags': 'Mounting 3.2mm 9775076960', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Mounting_Wuerth.3dshapes/Mounting_Wuerth_WA-SMSR-3.2mm_H7.6mm_ReverseMount_9775076960.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Mounting_Wuerth : Mounting_Wuerth_WA-SMSR-3.2mm_H7.6mm_ReverseMount_9775076960')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

