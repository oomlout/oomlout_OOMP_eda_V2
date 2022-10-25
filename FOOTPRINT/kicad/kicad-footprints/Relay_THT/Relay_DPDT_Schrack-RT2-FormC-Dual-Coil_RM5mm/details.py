
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Relay_THT"
    oIndex = "Relay_DPDT_Schrack-RT2-FormC-Dual-Coil_RM5mm"
    hexID = "FZKRELRELAYDPDTSCHRACKRT2FORMCDUALCOILRM5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Relay_DPDT_Schrack-RT2-FormC-Dual-Coil_RM5mm', 'description': 'Relay DPDT Schrack-RT2 RM5mm 16A 250V AC Form C http://www.te.com/commerce/DocumentDelivery/DDEController?Action=showdoc&DocId=Data+Sheet%7FRT2_bistable%7F1116%7Fpdf%7FEnglish%7FENG_DS_RT2_bistable_1116.pdf%7F1-1415537-8', 'tags': 'Relay DPDT Schrack-RT2 RM5mm 16A 250V AC Relay', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Relay_THT.3dshapes/Relay_DPDT_Schrack-RT2-FormC-Dual-Coil_RM5mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'oval'}})
    newPart['name'].append('Relay_THT : Relay_DPDT_Schrack-RT2-FormC-Dual-Coil_RM5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

