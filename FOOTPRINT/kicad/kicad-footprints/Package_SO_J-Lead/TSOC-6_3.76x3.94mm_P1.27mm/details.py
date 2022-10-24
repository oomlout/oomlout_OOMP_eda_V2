
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO_J-Lead"
    oIndex = "TSOC-6_3.76x3.94mm_P1.27mm"
    hexID = "FZKSOJLEADTSOC6376X394P127"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TSOC-6_3.76x3.94mm_P1.27mm', 'description': 'Maxim Integrated TSOC-6 D6+1,https://datasheets.maximintegrated.com/en/ds/DS2401.pdf, https://pdfserv.maximintegrated.com/land_patterns/90-0321.PDF', 'tags': 'TSOC-6', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO_J-Lead.3dshapes/TSOC-6_3.76x3.94mm_P1.27mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SO_J-Lead : TSOC-6_3.76x3.94mm_P1.27mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

