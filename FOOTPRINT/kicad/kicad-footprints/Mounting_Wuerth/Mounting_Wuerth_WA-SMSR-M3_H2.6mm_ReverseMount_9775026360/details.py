
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Mounting_Wuerth"
    oIndex = "Mounting_Wuerth_WA-SMSR-M3_H2.6mm_ReverseMount_9775026360"
    hexID = "FZKMONMONWASMSRM3H26RMOUNT97752636"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Mounting_Wuerth_WA-SMSR-M3_H2.6mm_ReverseMount_9775026360', 'description': 'Mounting Hardware, inside through hole M3, height 2.6, Wuerth electronics 9775026360 (https://katalog.we-online.com/em/datasheet/9775026360.pdf), generated with kicad-footprint-generator', 'tags': 'Mounting M3 9775026360', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Mounting_Wuerth.3dshapes/Mounting_Wuerth_WA-SMSR-M3_H2.6mm_ReverseMount_9775026360.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Mounting_Wuerth : Mounting_Wuerth_WA-SMSR-M3_H2.6mm_ReverseMount_9775026360')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

