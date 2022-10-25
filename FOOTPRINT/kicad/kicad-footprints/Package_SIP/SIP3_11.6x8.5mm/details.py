
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SIP"
    oIndex = "SIP3_11.6x8.5mm"
    hexID = "FZKSIPSIP3116X85"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SIP3_11.6x8.5mm', 'description': 'RECOM,R78EXX,https://www.recom-power.com/pdf/Innoline/R-78Exx-0.5.pdf', 'tags': 'SIP3 Regulator Module', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SIP.3dshapes/SIP3_11.6x8.5mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Package_SIP : SIP3_11.6x8.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

