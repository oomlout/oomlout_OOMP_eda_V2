
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Relay_SMD"
    oIndex = "Relay_SPDT_AXICOM_HF3Series_75ohms_Pitch1.27mm"
    hexID = "FZKRELAYSMRELAYSPDTAXICOMHF3SERIES75OHMSPITCH127"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Relay_SPDT_AXICOM_HF3Series_75ohms_Pitch1.27mm', 'description': 'hiqsdr.com/images/3/3e/Axicom-HF3.pdf', 'tags': 'AXICOM HF3-Series Relay Pitch 1.27mm 75ohm', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Relay_SMD.3dshapes/Relay_SPDT_AXICOM_HF3Series_75ohms_Pitch1.27mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Relay_SMD : Relay_SPDT_AXICOM_HF3Series_75ohms_Pitch1.27mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

