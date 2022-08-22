from snake import *

LEARN_RATE = 0.6
PRZEWIDYWALNOSC = 0.1

def rand_max(zbior:list):
    ind_max = []
    for i in range(len(zbior)):
        if zbior[i] == max(zbior):
            ind_max.append(i)
    return random.choice(ind_max)

def check_position(srodowisko: str, stany: dict):
    for key in stany.keys():
        if srodowisko == key:
            print(stany[srodowisko])
            return stany[srodowisko]


class Agent:

    def __init__(self, srodowisko: str):
        self.srodowisko = srodowisko
        self.stan = {}
        for x_p in range(-width, WIDTH+width, width):
            for y_p in range(-height, HEIGHT+height, height):
                for x_j in range(0, JEDZ_WIDTH, 120):
                    for y_j in range(0, JEDZ_HEIGHT, 80):
                        self.stan[f'{x_p} {y_p} {x_j} {y_j}'] = [0, 0, 0, 0]


    def predict_next(self, srodowisko, ilosc_gier):
        if random.randint(0, 10 + ilosc_gier // 55) == 2: return random.randint(0, 3)
        if max(self.stan.get(srodowisko)) == min(self.stan.get(srodowisko)): return random.randint(0, 3)
        return rand_max(self.stan.get(srodowisko))

    def update(self, player_food_pos):
        self.srodowisko = player_food_pos

    def learn(self, prev_predict, prev_pole, did_collide, did_lose):
        nagroda = 0

        if did_lose:
            nagroda = -1

        if did_collide:
            nagroda = 1

        maks_wartosc = max(self.stan.get(self.srodowisko))
        self.stan.get(prev_pole)[prev_predict] += LEARN_RATE * (
                nagroda + PRZEWIDYWALNOSC*maks_wartosc - self.stan.get(prev_pole)[prev_predict])


