
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "LED_THT"
    oIndex = "LED_VCCLite_5381H1_6.35x6.35mm"
    hexID = "FZKLLVCCLITE5381H1635X635"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LED_VCCLite_5381H1_6.35x6.35mm', 'description': 'Red 5381 Series LED VCCLite https://vcclite.com/wp-content/uploads/wpallimport/files/files/5381Series.pdf http://static.vcclite.com/pdf/Mounting%20Hole%20Pattern%202.pdf', 'tags': 'Red 5381 Series LED', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/LED_THT.3dshapes/LED_VCCLite_5381H1_6.35x6.35mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('LED_THT : LED_VCCLite_5381H1_6.35x6.35mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

