
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Crystal"
    oIndex = "Resonator_Murata_DSS6-3Pin_W7.0mm_H2.5mm"
    hexID = "FZKXRMDSS63PINW7H25"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Resonator_Murata_DSS6-3Pin_W7.0mm_H2.5mm', 'description': 'Ceramic Resomator/Filter Murata DSS6, http://cdn-reichelt.de/documents/datenblatt/B400/DSN6NC51H.pdf, length*width=7.0x2.5mm^2 package, package length=7.0mm, package width=2.5mm, 3 pins', 'tags': 'THT ceramic resonator filter DSS6', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Crystal.3dshapes/Resonator_Murata_DSS6-3Pin_W7.0mm_H2.5mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Crystal : Resonator_Murata_DSS6-3Pin_W7.0mm_H2.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

