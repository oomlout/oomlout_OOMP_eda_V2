
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Crystal"
    oIndex = "Resonator_Murata_CSTLSxxxG-3Pin_W8.0mm_H3.0mm"
    hexID = "FZKXRMCSTLSXXXG3PINW8H3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Resonator_Murata_CSTLSxxxG-3Pin_W8.0mm_H3.0mm', 'description': 'Ceramic Resomator/Filter Murata CSTLSxxxG, http://www.murata.com/~/media/webrenewal/support/library/catalog/products/timingdevice/ceralock/p17e.ashx, length*width=8.0x3.0mm^2 package, package length=8.0mm, package width=3.0mm, 3 pins', 'tags': 'THT ceramic resonator filter CSTLSxxxG', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Crystal.3dshapes/Resonator_Murata_CSTLSxxxG-3Pin_W8.0mm_H3.0mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Crystal : Resonator_Murata_CSTLSxxxG-3Pin_W8.0mm_H3.0mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

