
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Crystal"
    oIndex = "Resonator-2Pin_W10.0mm_H5.0mm"
    hexID = "FZKXR2PINW1H5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Resonator-2Pin_W10.0mm_H5.0mm', 'description': 'Ceramic Resomator/Filter 10.0x5.0 RedFrequency MG/MT/MX series, http://www.red-frequency.com/download/datenblatt/redfrequency-datenblatt-ir-zta.pdf, length*width=10.0x5.0mm^2 package, package length=10.0mm, package width=5.0mm, 2 pins', 'tags': 'THT ceramic resonator filter', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Crystal.3dshapes/Resonator-2Pin_W10.0mm_H5.0mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Crystal : Resonator-2Pin_W10.0mm_H5.0mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

