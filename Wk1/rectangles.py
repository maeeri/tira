def area(rec1, rec2, rec3):
    common_r1_r2 = common_area_coordinates(rec1, rec2)
    common_r1_r3 = common_area_coordinates(rec1, rec3)
    common_r2_r3 = common_area_coordinates(rec2, rec3)
    common_all = calculate_area(common_area_coordinates(rec1, common_r2_r3))
    areas = []
    common_areas = []
    recs = [rec1, rec2, rec3]
    c = [common_r1_r2, common_r1_r3, common_r2_r3]
    
    for r in recs:
        areas.append(calculate_area(r))
    for x in c:
        common_areas.append(calculate_area(x))
    return sum(areas) - sum(common_areas) + common_all
    
def calculate_area(r):
    x_length = abs(r[0]) + abs(r[2]) if r[0] <= 0 and r[2] >= 0 else abs(r[2] - r[0])
    y_length = abs(r[1]) + abs(r[3]) if r[1] <= 0 and r[3] >= 0 else abs(r[3] - r[1])
    return x_length * y_length

def common_area_coordinates(r1, r2):
    r1x1, r1y1, r1x2, r1y2 = r1
    r2x1, r2y1, r2x2, r2y2 = r2
    x1, y1, x2, y2 = 0,0,0,0
    no_common_area = r1x1 > r2x2 or r2x1 > r1x2 or r1y2 > r2y1 or r2y2 > r1y1
    if not no_common_area:
        x1 = max(r1x1, r2x1)
        x2 = min(r1x2, r2x2)
        y1 = min(r1y1, r2y1)
        y2 = max(r1y2, r2y2)
    return (x1, y1, x2, y2)

if __name__ == "__main__":
    rec1 = (-1,1,1,-1)
    rec2 = (0,3,2,0)
    rec3 = (0,2,3,-2)
    print(area(rec1,rec2,rec3)) # 16

    rec1 = (-1,2,2,-2)
    rec2 = (-1,3,0,2)
    rec3 = (0,3,2,-2)
    print(area(rec1,rec2,rec3)) # 15

    rec1 = (2,-1,3,-3)
    rec2 = (0,2,3,0)
    rec3 = (-3,0,1,-1)
    print(area(rec1,rec2,rec3)) # 12


#     Tasossa on kolme suorakulmiota, joiden sivut ovat vaaka- ja pystyakselien suuntaisia. Tehtäväsi on laskea sen alueen pinta-ala, jota peittää vähintään yksi annetuista suorakulmioista.

# Esimerkiksi seuraavassa kuvassa suorakulmioiden peittämän alueen pinta-ala on 16. Kuva vastaa koodipohjissa olevaa esimerkkiä.

# Voit olettaa, että kaikki koordinaatit ovat kokonaislukuja välillä −109…109
# .

# Huomaa, että on liian hidasta käydä läpi kaikki pisteet suorakulmioiden alueelta, vaan sinun tulee keksiä tehokkaampi matemaattinen ratkaisu.

# Toteuta funktio area(rec1, rec2, rec3), joka antaa kysytyn pinta-alan. Funktiolle annetaan kolme tuplea, joista jokainen määrittelee yhden suorakulmion. Jokaisessa tuplessa on neljä kokonaislukua x1
# , y1
# , x2
#  ja y2
# : suorakulmion vasen ylänurkka on (x1,y1)
#  ja oikea alanurkka on (x2,y2)
# .

# Toteuta funktio tiedostoon rectangles.py.