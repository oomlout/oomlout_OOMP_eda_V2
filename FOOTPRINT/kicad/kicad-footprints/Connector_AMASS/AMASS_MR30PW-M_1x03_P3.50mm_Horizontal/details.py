
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_AMASS"
    oIndex = "AMASS_MR30PW-M_1x03_P3.50mm_Horizontal"
    hexID = "FZKCNAMASSAMASSMR3PWM1X3P35HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'AMASS_MR30PW-M_1x03_P3.50mm_Horizontal', 'description': 'Connector XT30 Horizontal PCB Male, https://www.tme.eu/en/Document/5e47640ba39fa492dbd4c0f4c8ae7b93/MR30PW%20SPEC.pdf', 'tags': 'RC Connector XT30', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_AMASS.3dshapes/AMASS_MR30PW-M_1x03_P3.50mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_AMASS : AMASS_MR30PW-M_1x03_P3.50mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

