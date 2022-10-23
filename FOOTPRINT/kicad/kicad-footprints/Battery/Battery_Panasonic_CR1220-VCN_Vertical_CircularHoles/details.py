
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Battery"
    oIndex = "Battery_Panasonic_CR1220-VCN_Vertical_CircularHoles"
    hexID = "FZKBATBATPANASONICCR122VCNVERTICALCIRCULARH"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Battery_Panasonic_CR1220-VCN_Vertical_CircularHoles', 'description': 'Panasonic CR-1220/VCN battery, https://industrial.panasonic.com/cdbs/www-data/pdf2/AAA4000/AAA4000D140.PDF', 'tags': 'battery CR-1220 coin cell vertical', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Battery.3dshapes/Battery_Panasonic_CR1220-VCN_Vertical_CircularHoles.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Battery : Battery_Panasonic_CR1220-VCN_Vertical_CircularHoles')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

