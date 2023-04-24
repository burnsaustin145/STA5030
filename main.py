import pickle
import pprint as pp
import csv


def write_csv(team, game_ids, dat, to_file, write, labels, stats_keys):
    write.writerow(labels)
    for id in game_ids:
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
        for stat in stats_keys:
            currRow.append(dat[id]['home']['statistics'][stat])
        write.writerow(currRow)
    to_file.close()


def writeCSV2(gameIds, dat, toFile, write, labels, statsKeys):
    labels.append("home_away")
    write.writerow(labels)
    for gameId in gameIds:
        for location in ("home", "away"):
            currRow = [gameId]
            teamPts = dat[gameId][location]['points']
            otherPts = dat[gameId]['home' if location == 'away' else 'away']['points']
            currRow.append(teamPts)
            currRow.append('win' if teamPts > otherPts else 'loss')
            try:
                currRow.append(dat[gameId]['attendance'])
            except:
                currRow.append("no_info")
            for stat in statsKeys:
                currRow.append(dat[gameId][location]['statistics'][stat])
            currRow.append(location)
            write.writerow(currRow)
    toFile.close()


def generate_initial_labels():
    gameIds = list(dat.keys())
    print("got ids")
    statsKeys = list(dat[gameIds[0]]['home']['statistics'])
    print(statsKeys)
    statsKeys.remove('most_unanswered')
    statsKeys.remove('periods')
    # from dat: id->home/away->points
    # id->home/away->statistics->{stats list all vars here}
    # id->attendance
    return statsKeys, gameIds


#writing csv for initial variable set
def generate_vars1(statsKeys, gameIds):
    with open('tidy200.csv', mode='w') as toFile:
        write = csv.writer(toFile, delimiter=',', quotechar='"')
        columnLabels = ['Game Id', 'points', 'result', 'attendance']
        for lab in statsKeys:
            columnLabels.append(lab)
        write_csv('home', gameIds, dat, toFile, write, columnLabels, statsKeys)


# this generate funciton adds home/away variable (should refactor to select for multiple vars??
def generate_vars2(statsKeys, gameIds):
    with open('tidy200_conf.csv', mode='w') as toFile:
        write = csv.writer(toFile, delimiter=',', quotechar='"')
        columnLabels = ['Game Id', 'points', 'result', 'attendance']
        for lab in statsKeys:
            columnLabels.append(lab)
        writeCSV2(gameIds, dat, toFile, write, columnLabels, statsKeys)


# some initial testing
if __name__ == "__main__":
    try:
        with open('pickledDat200.pickle', 'rb') as handle:
            dat = pickle.load(handle)
        print("got dat")
    except:
        print("open pickle jar error")

# %% creating tidy200.csv for initial testing
# keys, gameIds = generateInitialLabels()
# varSet1(keys, gameIds)

# adding home/away stat to data
keys, game_ids = generate_initial_labels()
generate_vars2(keys, game_ids)




