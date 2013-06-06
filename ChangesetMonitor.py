#!/usr/bin/python
# -*- coding: cp1252 -*-
import OsmApi
import csv
import os
os.chdir('~/python/\\')

#nom_csv='stats-cap103-20130-03-28-05-05.csv'
nom_csv='stats-cap103-2013-05-06-05-31.csv'
#nom_csv='stats-cap103-2013-06-04.csv'
#date_from="2013-05-20T06:00:00Z"
#date_to="2013-05-29T23:59:00Z"
#date_from="2013-06-03T06:00:00Z"
#date_to="2013-06-03T23:59:00Z"
#date_from="2013-03-28T06:00:00Z"
#date_to="2013-05-05T23:59:00Z"
date_from="2013-05-06T06:00:00Z"
date_to="2013-06-01T00:00:00Z"
#date_from="2013-06-04T06:00:00Z"
#date_to="2013-06-04T23:59:00Z"
nom_csv='stats-cap103-2013-05-16-05-31.csv'
date_from="2013-05-16T06:00:00Z"
date_to="2013-05-31T23:59:00Z"
#====

# April
#=========================================================
#=========================================================
# April
#=========================================================
nom_csv='stats-cap103-2013-04-01-04-07.csv'
date_from="2013-04-01T06:00:00Z"
date_to="2013-04-07T23:59:00Z"
nom_csv='stats-cap103-2013-04-08-04-14.csv'
date_from="2013-04-08T06:00:00Z"
date_to="2013-04-14T23:59:00Z"
nom_csv='stats-cap103-2013-04-15-04-21.csv'
date_from="2013-04-15T06:00:00Z"
date_to="2013-04-21T23:59:00Z"
nom_csv='stats-cap103-2013-04-22-04-28.csv'
date_from="2013-04-22T13:00:00Z"
date_to="2013-04-28T23:59:00Z"
nom_csv='stats-cap103-2013-04-29-04-30.csv'
date_from="2013-04-29T13:00:00Z"
date_to="2013-04-30T23:59:00Z"

#=========================================================
# May
#=========================================================
#=========================================================
# May
#=========================================================
nom_csv='stats-cap103-2013-05-01-05-05.csv'
date_from="2013-05-01T06:00:00Z"
date_to="2013-05-05T23:59:00Z"
nom_csv='stats-cap103-2013-05-06-05-12.csv'
date_from="2013-05-06T06:00:00Z"
date_to="2013-05-12T23:59:00Z"
nom_csv='stats-cap103-2013-05-13-05-19.csv'
date_from="2013-05-13T06:00:00Z"
date_to="2013-05-19T23:59:00Z"
nom_csv='stats-cap103-2013-05-20-05-26.csv'
date_from="2013-05-20T13:00:00Z"
date_to="2013-05-26T23:59:00Z"
nom_csv='stats-cap103-2013-05-27-06-02.csv'
date_from="2013-05-27T13:00:00Z"
date_to="2013-06-02T23:59:00Z"

#=========================================================

min_lon=-72.266
max_lon=-71.7
min_lat=19.443
max_lat=19.793
users = ["Alcin Stevenson", "jean presler", "WingedStone", "Guensmork", "richelet",
         "bonhommebrunie", "jeandany", "jeune", "rlouino", "wilner",
         "lubin nancy", "wilford", "Perest Jonas", "senatusgesner",
         "vetillac seneque", "jaakkoh", "Heurtelou",
         "Tinono", "nadege michaud", "fenel", "ALCE SamuelPaul",
         "worldwidewolford", "wonderchook", "Mdr", "MJNcs", "lyonel_lav", "Marion Barry",
         "patricia_beauvoir", "Souvenise Saint-Jean", "Gine", "alexis josy",
         "eustache70", "Adler Salvador", "SergeDorval", "pierre eddy",
         "Wildbill", "rab", "manic12"
        ]

users[1] = ["Bloocinsha","cinalien ferry","saint jean conslyn","dagno","Frandieu","chedo","Elbrenard Dunel","jean roudeline","Roody sinsmyr","Lovly Duitch Turenne"]
users[2] = ["Didygroove","leslymc4","EDOUARD Cherline","westner","cadet junior","Sterlin Reginald","maudeline","Fleurette","chedelyn seide","vankedly"]
users[3] = ["Noel Saint-clair","Scott Jojo","Aristilde","Gladson Ralph","cherenfant","sandrosaintus","Emile Merline","sodany","youdly jean pierre","Rodney Simeon"]
users[4] = ["Jean Pierre D","Wood Louis","jean jean baptiste","Renel augustin","garcon frantz","nyrva etienne","mackenlove","Evens Louis","fricotfils","josias joseph"]
users[5] = ["John Carlo","rodenec","Walky Sinsmyr","Luny-Fred saint-vil","Emmanuel CHARLES","Jodelin Pierre","valmyr","mijo25","Adm Rubens","sodany"]
#users[5] = ["Walky Sinsmyr","Luny-Fred saint-vil","Emmanuel CHARLES","Jodelin Pierre","valmyr","mijo25","Adm Rubens","sodany"]
users[6] = ["BENJAMIN Johnson","byssainthe-2","mayuma","wesly joseph","similia joseph","Sylrose Charles","POLYMICE Dielinx","valdyr","klakey","Florival Acci-Rolain"]
users[7] = ["Debreus Rei", "michel evens","Jean Bully","Adler Salvador","delchy","joseph roberto","schneider alcereste","pierre louis fritzner","Bregneve","Michel Jacqueson",
"wedens louisius","Casseus Peres","Jeudyphilius anita","Xapitoun", "ALCE SamuelPaul","CERISIER Judith"]
# bbox=-72.266,19.443,-71.7,19.793 
# Haiti CAP103 bbox: min_lon=-72.266, max_lon=-72.49, min_lat=19.443, max_lat=19.793
# Haiti bbox: min_lon=-74.83, max_lon=-72.49, min_lat=17.4, max_lat=20.43
# PaP bbox: min_lon=-72.452, max_lat=18.672, max_lon=-71.178, min_lat=18.468

def getChangesets(username=None):
    changesets = osmApi.ChangesetsGet(min_lon, min_lat, max_lon, max_lat,
            username=username, closed_after=date_from,
            created_before=date_to)
    return changesets
# {u'action': u'create', u'data': {u'changeset': 16327554, u'uid': 1339602, u'timestamp': u'2013-05-28T18:08:53Z', u'lon': -71.9755596, u'visible': True, u'version': 1, u'user': u'John Carlo', u'lat': 19.6543342,
# u'tag': {u'addr:housenumber': u'0869H-10-100', u'addr:street': u'Village Nativity Terrier-Rouge'}, u'id': 2323372166L},
# u'type': u'node'}

def getChangesetStats(cid):
    stat= {"changeset":0,"node_c":0, "way_c":0, "relation_c":0,"node_m":0, "way_m":0, "relation_m":0,"node_d":0, "way_d":0, "relation_d":0}
    for changesetData in osmApi.ChangesetDownload(cid):
        #print changesetData
        if(changesetData["action"] == "create") :
            if changesetData["type"] == "node" :
                stat["node_c"] += 1
            elif changesetData["type"] == "way":
                stat["way_c"] += 1
            elif changesetData["type"] == "relation":
                stat["relation_c"] += 1    
        elif(changesetData["action"] == "modify") :
            if changesetData["type"] == "node" :
                stat["node_m"] += 1
            elif changesetData["type"] == "way":
                stat["way_m"] += 1
            elif changesetData["type"] == "relation":
                stat["relation_m"] += 1    
        elif(changesetData["action"] == "delete") :
            if changesetData["type"] == "node" :
                stat["node_d"] += 1
            elif changesetData["type"] == "way":
                stat["way_d"] += 1
            elif changesetData["type"] == "relation":
                stat["relation_d"] += 1    
        else:
            print "ERROR" 
    return stat

def updateStat(dict1, dict2):
    return dict((n, dict2.get(n, 0)+ dict2.get(n, 0)) for n in set(dict1)|set(dict2))
    

#
# Action begins here!
print "========================================================================="
print "ChangesetMonitor_cap103.py"
print " Pierre Beland, 06-2013"
print " Statistics of history of contribution by user and team"
print "date range and bbox as input"
print "Objects (ie. nodes, ways, relations) created, modified and deleted"
print "Original script (Seb's stats script v0.4 ) written by Sebastien Pierrel produced only statistics for objects created"
print "========================================================================="
print "Input variables "
print "list of users by team : vectors users [1] to [6]"
print "date_from=" + str(date_from)
print "date_to=" + str(date_to)
print "bbox : min_lon=" + str(min_lon) + ", max_lon=" + str(max_lon) + ", min_lat=" + str(min_lat) + ", max_lat=" + str(max_lat)

print "Checking changesets for "
osmApi = OsmApi.OsmApi(appid = "api.openstreetmap.fr",debug=False)
csv = open(nom_csv, 'wb')
csv.write("ekip, user, changeset, node_c,way_c,relation_c, node_m,way_m,relation_m, node_d,way_d,relation_d \n")
csv.flush()
nom_csv_team=nom_csv+'_team'
csv_team = open(nom_csv_team, 'wb')
csv_team.write("ekip, user, changeset, node_c,way_c,relation_c, node_m,way_m,relation_m, node_d,way_d,relation_d \n")
csv_team.flush()
print "trainee            number of changesets"
for ekip in range(1,8):
    stats_team= {"changeset":0,"node_c":0, "way_c":0, "relation_c":0,"node_m":0, "way_m":0, "relation_m":0,"node_d":0, "way_d":0, "relation_d":0}
    print "\n ekip " + str(ekip)
    for user in users[ekip]:
        stats = {"changeset":0,"node_c":0, "way_c":0, "relation_c":0,"node_m":0, "way_m":0, "relation_m":0,"node_d":0, "way_d":0, "relation_d":0}
        changesets = getChangesets(username=user)
        nb_changesets=len(changesets)
        # print string.rjust(`x`, 2), string.rjust(`x*x`, 3),
        #print str(user) +"\t\t" + str(nb_changesets)
        print'%-20s %6d' % (user,nb_changesets)
        #print  changesets
        for id in changesets:
            csstat= getChangesetStats(id)
            #print changeset
            stats["changeset"] += 1
            stats["node_c"] += csstat["node_c"]
            stats["way_c"]  += csstat["way_c"]
            stats["relation_c"] += csstat["relation_c"] 
            stats["node_m"] += csstat["node_m"]
            stats["way_m"]  += csstat["way_m"]
            stats["relation_m"] += csstat["relation_m"] 
            stats["node_d"] += csstat["node_d"]
            stats["way_d"]  += csstat["way_d"]
            stats["relation_d"] += csstat["relation_d"] 
    #        stats = updateStat(stats, getChangesetStats(id))
    #    print user + ", " + str(len(changesets)) + ", " + str(stats["node"]) + ", " + str(stats["way"]) + ", " + str(stats["relation"])
        stats_team["changeset"] += stats["changeset"]
        stats_team["node_c"] += stats["node_c"]
        stats_team["way_c"]  += stats["way_c"]
        stats_team["relation_c"] += stats["relation_c"] 
        stats_team["node_m"] += stats["node_m"]
        stats_team["way_m"]  += stats["way_m"]
        stats_team["relation_m"] += stats["relation_m"] 
        stats_team["node_d"] += stats["node_d"]
        stats_team["way_d"]  += stats["way_d"]
        stats_team["relation_d"] += stats["relation_d"] 
        csv.write(str(ekip) +", " +str(user) +", " + str(len(changesets)) + ", " + str(stats["node_c"]) + ", " + str(stats["way_c"]) + ", " + str(stats["relation_c"])+ ", " + str(stats["node_m"]) + ", " + str(stats["way_m"]) + ", " + str(stats["relation_m"])+ ", " + str(stats["node_d"]) + ", " + str(stats["way_d"]) + ", " + str(stats["relation_d"])  + "\n")
        csv.flush()
    # end of team - print in summary file by team
    csv_team.write(str(ekip) +", " + str(date_from[1:10])+" - " + str(date_to[1:10])+", " + str(stats_team["changeset"]) + ", " + str(stats_team["node_c"]) + ", " + str(stats_team["way_c"]) + ", " + str(stats_team["relation_c"])+ ", " + str(stats_team["node_m"]) + ", " + str(stats_team["way_m"]) + ", " + str(stats_team["relation_m"])+ ", " + str(stats_team["node_d"]) + ", " + str(stats_team["way_d"]) + ", " + str(stats_team["relation_d"])  + "\n")
    csv_team.flush()
csv.close()
print "Done."