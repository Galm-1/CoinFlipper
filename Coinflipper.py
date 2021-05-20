# Ecrit ton programme ici ;-)
import random
numberOfStreak = 0
n_runs = 10000
flips_per_run = 100
streak_length = 6

for experimentNumber in range(n_runs) :
    #Create a flips_per_run list
    HeadorTail = []
    for flips in range(flips_per_run):
        if random.randint(0,1) == 0:
            HeadorTail.append("H")
        else:
            HeadorTail.append("T")

    # check if you got a streak
    current_streak = 1
    previous_flip = None
    for flips in HeadorTail:
        if flips == previous_flip:
            current_streak += 1
            if current_streak == streak_length:
                numberOfStreak += 1
                break
        else:
            current_streak = 0
        previous_flip = flips

percentageofstreak = numberOfStreak / n_runs
print(" Pourcentage est : " + str(percentageofstreak))
print(" Soi : " + str(percentageofstreak*100) + "%")
