from django.db import connection
import pandas as pd

def SelectQueryDF(query):
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            columns = [col[0] for col in cursor.description]
            result = cursor.fetchall()
            
            df = pd.DataFrame(result, columns=columns)
            return True, df            
    except Exception as e:
        print(e)
        return False, None
    
def SelectQueryListDict(query):
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            columns = [col[0] for col in cursor.description]
            result = cursor.fetchall()
            
            # Convert each row to a dictionary
            data = [{columns[i]: row[i] for i in range(len(columns))} for row in result]
            
            return True, data
    except Exception as e:
        print(e)
        return False, None