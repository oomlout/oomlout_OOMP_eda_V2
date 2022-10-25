
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Relay_THT"
    oIndex = "Relay_SPST_Schrack-RT1-16A-FormA_RM5mm"
    hexID = "FZKRELRELAYSPSTSCHRACKRT116AFORMARM5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Relay_SPST_Schrack-RT1-16A-FormA_RM5mm', 'description': 'Relay SPST Schrack-RT2 RM5mm 16A 250V AC Form C http://www.te.com/commerce/DocumentDelivery/DDEController?Action=srchrtrv&DocNm=RT2_reflow&DocType=DS&DocLang=EN', 'tags': 'Relay SPST Schrack-RT2 RM5mm 16A 250V AC Relay', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Relay_THT.3dshapes/Relay_SPST_Schrack-RT1-16A-FormA_RM5mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'oval'}})
    newPart['name'].append('Relay_THT : Relay_SPST_Schrack-RT1-16A-FormA_RM5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

