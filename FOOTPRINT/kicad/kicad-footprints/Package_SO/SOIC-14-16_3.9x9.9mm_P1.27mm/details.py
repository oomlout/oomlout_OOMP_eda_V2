
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "SOIC-14-16_3.9x9.9mm_P1.27mm"
    hexID = "FZKSOSOIC141639X99P127"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SOIC-14-16_3.9x9.9mm_P1.27mm', 'description': 'SOIC, 16 Pin package with pin 2 and 13 removed for voltage clearance  (UCC256301, https://www.ti.com/lit/ds/symlink/ucc256301.pdf)', 'tags': 'SOIC SO', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/SOIC-16_3.9x9.9mm_P1.27mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_SO : SOIC-14-16_3.9x9.9mm_P1.27mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

