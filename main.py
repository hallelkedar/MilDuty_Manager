from soldier_manager import add_soldier, remove_soldier, get_all_soldiers
from duty_manager import add_duty_to_soldier, update_duty_status, get_soldier_duties
"""
מערכת ניהול תורנויות חיילים
"""

# ============================================================================
# main.py
# אחריות: תפריט ראשי, קלט מהמשתמש, ניתוב לפונקציות
# ============================================================================
MAIN_MENU = """
=== מערכת לניהול תורנויות חיילים ===
1. הוספת חייל חדש
2. הסרת חייל מהמערכת
3. צפייה ברשימת כל החיילים
4. שיבוץ חייל לתורנות
5. עדכון סטטוס תורנות
6. צפייה בתורנויות של חייל
7. יציאה מהמערכת
==================================
"""
NUM_OF_OPTIONS = 7

def show_menu() -> None:
    """
    מציגה את התפריט הראשי למשתמש.
    
    מקבלת: כלום
    מחזירה: כלום (מדפיסה לקונסול)
    
    למה הפונקציה קיימת:
    הפרדה בין הצגת התפריט לבין הלוגיקה העסקית.
    אם נרצה לשנות את התצוגה, נשנה רק כאן.
    """
    print(MAIN_MENU, end="")

def get_user_choice() -> str:
    """
    מקבלת בחירה מהמשתמש.
    
    מקבלת: כלום
    מחזירה: מחרוזת המייצגת את בחירת המשתמש
    
    למה הפונקציה קיימת:
    הפרדת קבלת קלט מהמשתמש מהלוגיקה של עיבוד הבחירה.
    מאפשר להחליף את שיטת הקלט בעתיד (למשל, GUI).
    """
    user_choice = input(f"Enter your choice (1 - {NUM_OF_OPTIONS}): ")
    return user_choice

def handle_add_soldier() -> None:
    """
    מטפלת בתהליך הוספת חייל חדש.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    מפרידה בין הקלט/פלט לבין הלוגיקה העסקית.
    main.py אחראי על אינטראקציה עם המשתמש,
    soldier_manager.py אחראי על הלוגיקה.
    """
    soldier_id = int(input("הכנס מספר אישי: "))
    name = input("הכנס שם: ")
    try:
        add_soldier(soldier_id, name)
        print("חייל נוסף בהצלחה ✓")
    except ValueError as e:
        print(f"""
            ✗ שגיאה: {e}
            !אנא הכנס מספר תקין וחדש
            """)

def handle_remove_soldier() -> None:
    """
    מטפלת בתהליך הסרת חייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    soldier_id = int(input("הכנס מספר אישי: "))
    try:
        remove_soldier(soldier_id)
        print("חייל הוסר בהצלחה ✓")
    except ValueError as e:
        print(f"""
            ✗ שגיאה: {e}
            !אנא הכנס מספר תקין וקיים
            """)

def handle_view_soldiers() -> None:
    """
    מטפלת בתהליך הצגת כל החיילים.
    קוראת לפונקציה המתאימה ומציגה את התוצאה.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    הפרדה בין קבלת הנתונים לבין הצגתם.
    """
    solider_list = get_all_soldiers()
    if solider_list:
        for solider in solider_list:
            print(f"""
                  Name - {solider["name"]}
                  ID Number - {solider["id"]})
                  """)
    else:
        print("Soldiers list is empty.")

def handle_add_duty() -> None:
    """
    מטפלת בתהליך הוספת תורנות לחייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    soldier_id = int(input("הכנס מספר אישי: "))
    duty_name = input("הכנס שם תורנות: ")
    day = input("הכנס יום: ")
    try:
        add_duty_to_soldier(soldier_id, duty_name, day)
        print("תורנות נוספה בהצלחה ✓")
    except (ValueError, KeyError) as e:
        print(f"""
            ✗ שגיאה: {e}
            !אנא הכנס מספר תקין קיים, שם משימה תקין ויום אפשרי בשבוע
            """)


def handle_update_duty_status() -> None:
    """
    מטפלת בתהליך עדכון סטטוס תורנות.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    soldier_id = int(input("הכנס מספר אישי: "))
    duty_name = input("הכנס שם תורנות: ")
    new_status = input("הכנס סטטוס תורנות: ")
    try:
        update_duty_status(soldier_id, duty_name, new_status)
        print("תורנות נוספה בהצלחה ✓")
    except (ValueError, KeyError) as e:
        print(f"""
            ✗ שגיאה: {e}
            !אנא הכנס מספר תקין קיים, שם משימה תקין וסטטוס תקין
            """)



def handle_view_soldier_duties() -> None:
    """
    מטפלת בתהליך הצגת תורנויות של חייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    
    soldier_id = int(input("הכנס מספר אישי: "))
    try:
        soldier_duties = get_soldier_duties(soldier_id)
        if soldier_duties:
            for i, duty in enumerate(soldier_duties):
                print(f"{i+1} - {duty}")
        else:
            print("Soldier has no duties.")

    except KeyError as e:
        print(f"""
            ✗ שגיאה: {e}
            !אנא הכנס מספר תקין קיים
            """)


def main() -> None:
    """
    הפונקציה הראשית של התוכנית.
    מריצה לולאה ראשית שמציגה תפריט, מקבלת בחירה ומפעילה פעולה.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    נקודת הכניסה לתוכנית. מנהלת את הזרימה הראשית.
    """
    pass