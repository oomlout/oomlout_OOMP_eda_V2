
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Relay_THT"
    oIndex = "Relay_SPDT_Schrack-RT1-16A-FormC_RM5mm"
    hexID = "FZKRELRELAYSPDTSCHRACKRT116AFORMCRM5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Relay_SPDT_Schrack-RT1-16A-FormC_RM5mm', 'description': 'Relay SPST Schrack-RT1 RM5mm 16A 250V AC Form C http://image.schrack.com/datenblaetter/h_rt114012--_de.pdf', 'tags': 'Relay SPST Schrack-RT1 RM5mm 16A 250V AC Relay', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Relay_THT.3dshapes/Relay_DPDT_Schrack-RT2-FormC_RM5mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'oval'}})
    newPart['name'].append('Relay_THT : Relay_SPDT_Schrack-RT1-16A-FormC_RM5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

