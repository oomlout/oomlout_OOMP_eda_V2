
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "Choke_EPCOS_B82722A"
    hexID = "FZKINCHOKEEPCOSB82722A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Choke_EPCOS_B82722A', 'description': 'Current-Compensated Ring Core Double Chokes, EPCOS, B82722A, 22.3mmx22.7mm, https://en.tdk.eu/inf/30/db/ind_2008/b82722a_j.pdf', 'tags': 'chokes epcos tht', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/Choke_EPCOS_B82722A.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : Choke_EPCOS_B82722A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

