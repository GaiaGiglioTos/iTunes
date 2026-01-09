from database.DB_connect import DBConnect
from model.album import Album


class DAO():

    @staticmethod
    def getAlbum(d):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select a.*
from album a, track t
where a.AlbumId = t.AlbumId 
group by a.AlbumId 
having (sum(t.Milliseconds)/60000) > %s
"""

        cursor.execute(query,(d,))

        for row in cursor:
            result.append(Album(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getArchi(idMap):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct t1.AlbumId as id1, t2.AlbumId as id2
from playlisttrack p1, playlisttrack p2, track t1, track t2
where p1.PlaylistId = p2.PlaylistId 
and t1.AlbumId < t2.AlbumId 
and p1.TrackId = t1.TrackId 
and p2.TrackId = t2.TrackId """

        cursor.execute(query)

        for row in cursor:
            if row["id1"] in idMap and row["id2"] in idMap:
                result.append((idMap[row["id1"]], idMap[row["id2"]]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getDurata(id):
        conn = DBConnect.get_connection()

        cursor = conn.cursor(dictionary=True)
        query = """select sum(t.Milliseconds)/60000 as d
from track t
where t.AlbumId = %s """

        cursor.execute(query,(id,))
        row = cursor.fetchone()


        cursor.close()
        conn.close()
        return row["d"]

