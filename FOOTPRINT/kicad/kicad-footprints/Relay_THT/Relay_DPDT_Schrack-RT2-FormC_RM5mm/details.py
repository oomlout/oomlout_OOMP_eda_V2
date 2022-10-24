
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Relay_THT"
    oIndex = "Relay_DPDT_Schrack-RT2-FormC_RM5mm"
    hexID = "FZKRELRELAYDPDTSCHRACKRT2FORMCRM5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Relay_DPDT_Schrack-RT2-FormC_RM5mm', 'description': 'Relay DPDT Schrack-RT2 RM5mm 16A 250V AC Form C http://www.te.com/commerce/DocumentDelivery/DDEController?Action=srchrtrv&DocNm=RT2_reflow&DocType=DS&DocLang=EN', 'tags': 'Relay DPDT Schrack-RT2 RM5mm 16A 250V AC Relay', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Relay_THT.3dshapes/Relay_DPDT_Schrack-RT2-FormC_RM5mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'oval'}})
    newPart['name'].append('Relay_THT : Relay_DPDT_Schrack-RT2-FormC_RM5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

