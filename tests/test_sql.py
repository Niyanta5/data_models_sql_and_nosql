import psycopg2

def test_sql_relationships():
    conn = psycopg2.connect("postgresql://user:password@localhost:5432/ecommerce")
    cursor = conn.cursor()
    
    # Ensure orders have valid users
    cursor.execute("""
        SELECT COUNT(*) FROM orders 
        WHERE user_id NOT IN (SELECT user_id FROM users)
    """)
    assert cursor.fetchone()[0] == 0, "Orphaned orders exist!"