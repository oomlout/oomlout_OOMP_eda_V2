
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "SOIC-8-N7_3.9x4.9mm_P1.27mm"
    hexID = "FZKSOSOIC8N739X49P127"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SOIC-8-N7_3.9x4.9mm_P1.27mm', 'description': '8-Lead Plastic Small Outline (SN) - Narrow, 3.90 mm Body [SOIC], pin 7 removed (Microchip Packaging Specification 00000049BS.pdf, http://www.onsemi.com/pub/Collateral/NCP1207B.PDF)', 'tags': 'SOIC 1.27', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/SOIC-8-N7_3.9x4.9mm_P1.27mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SO : SOIC-8-N7_3.9x4.9mm_P1.27mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

