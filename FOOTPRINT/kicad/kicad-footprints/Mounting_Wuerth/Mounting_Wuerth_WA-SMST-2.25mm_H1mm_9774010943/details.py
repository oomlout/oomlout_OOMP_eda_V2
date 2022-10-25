
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Mounting_Wuerth"
    oIndex = "Mounting_Wuerth_WA-SMST-2.25mm_H1mm_9774010943"
    hexID = "FZKMONMONWASMST225H197741943"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Mounting_Wuerth_WA-SMST-2.25mm_H1mm_9774010943', 'description': 'Mounting Hardware, inside through hole 2.25mm, height 1, Wuerth electronics 9774010943 (https://katalog.we-online.de/em/datasheet/9774010943.pdf), generated with kicad-footprint-generator', 'tags': 'Mounting 2.25mm 9774010943', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Mounting_Wuerth.3dshapes/Mounting_Wuerth_WA-SMST-2.25mm_H1mm_9774010943.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Mounting_Wuerth : Mounting_Wuerth_WA-SMST-2.25mm_H1mm_9774010943')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

