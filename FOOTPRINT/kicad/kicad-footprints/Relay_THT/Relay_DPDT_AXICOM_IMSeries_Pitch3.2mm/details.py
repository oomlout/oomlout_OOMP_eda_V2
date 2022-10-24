
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Relay_THT"
    oIndex = "Relay_DPDT_AXICOM_IMSeries_Pitch3.2mm"
    hexID = "FZKRELRELAYDPDTAXICOMIMSERIESPITCH32"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Relay_DPDT_AXICOM_IMSeries_Pitch3.2mm', 'description': 'AXICOM IM-Series Relays, DPDR, Pitch 3.2mm, http://www.te.com/commerce/DocumentDelivery/DDEController?Action=showdoc&DocId=Specification+Or+Standard%7F108-98001%7FV%7Fpdf%7FEnglish%7FENG_SS_108-98001_V_IM_0614_v1.pdf%7F4-1462039-1', 'tags': 'AXICOM IM-Series Relay DPDR Pitch 3.2mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Relay_THT.3dshapes/Relay_DPDT_AXICOM_IMSeries_Pitch3.2mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Relay_THT : Relay_DPDT_AXICOM_IMSeries_Pitch3.2mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

