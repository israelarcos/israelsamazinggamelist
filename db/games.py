import sqlite3
from sqlite3 import Error
from .connection import create_connection


def insert_game(data):
    conn = create_connection()
    sql = """ INSERT INTO games (title, category, duration, game_path, description) 
                VALUES(?, ?, ?, ?, ?)
    """

    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("New game added")
        return True, cur.lastrowid
    except Error as e:
        print("Error inserting new game:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()

def update_game(_id, data):
    conn = create_connection()

    sql = f""" UPDATE games SET  
                            title = ?,
                            category = ?,
                            duration = ?,
                            playedtime = ?,
                            game_path = ?,
                            description = ?
            WHERE game_id = {_id}

    """

    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("Game updated")
        return True
    except Error as e:
        print("Error updating game: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def delete_game(_id):
    conn = create_connection()
    sql = f"DELETE FROM games WHERE game_id = {_id}"


    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print("Game deleted")
        return True
    except Error as e:
        print("Error Deleting game:" + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_all_games():
    conn = create_connection()
    sql = "SELECT * FROM games"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        games = cur.fetchall()
        return games
    except Error as e:
        print("Error selecting all games: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_game_by_id(_id):
    conn = create_connection()
    sql = f"SELECT * FROM games WHERE game_id = {_id}"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        game = cur.fetchone()
        return game
    except Error as e:
        print("Error selecting game by id: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_game_by_title(title):
    conn = create_connection()
    sql = f"SELECT * FROM games WHERE title LIKE '%{title}%'"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        games = cur.fetchall()
        return games
    except Error as e:
        print("Error selecting game by title: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_game_by_category(category):
    conn = create_connection()
    sql = f"SELECT * FROM games WHERE category LIKE '%{category}%'"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        games = cur.fetchall()
        return games
    except Error as e:
        print("Error Selecting game by category: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


