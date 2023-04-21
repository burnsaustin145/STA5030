import pickle
import pprint as pp
import csv


def writeCSV(team, gameIds, dat, toFile, write):
    for id in gameIds:
        currRow = []
        currRow.append(id)
        teamPts = dat[id][team]['points']
        otherPts = dat[id]['home' if team == 'away' else 'away']['points']
        currRow.append(teamPts)
        currRow.append('win' if teamPts > otherPts else 'loss')
        try:
            currRow.append(dat[id]['attendance'])
        except:
            currRow.append("noinfo")
        print("tie??" if teamPts == otherPts else "")
        for stat in statsKeys:
            currRow.append(dat[id]['home']['statistics'][stat])
        write.writerow(currRow)
    toFile.close()

try:
    with open('pickledDat200.pickle', 'rb') as handle:
        dat = pickle.load(handle)
    print("got dat")
except:
    print("open pickle jar error")


gameIds = list(dat.keys())
print("got ids")
statsKeys = list(dat[gameIds[0]]['home']['statistics'])
print(statsKeys)
statsKeys.remove('most_unanswered')
statsKeys.remove('periods')
# from dat: id->home/away->points
# id->home/away->statistics->{stats list all vars here}
# id->attendance
with open('tidy200', mode='w') as toFile:
    write = csv.writer(toFile, delimiter=',', quotechar='"')
    writeCSV('home', gameIds, dat, toFile, write)


