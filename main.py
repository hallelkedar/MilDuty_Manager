from soldier_manager import add_soldier, remove_soldier, get_all_soldiers
from duty_manager import add_duty_to_soldier, update_duty_status, get_soldier_duties
from art import SOLDIER_ART
"""
מערכת ניהול תורנויות חיילים
"""

# ============================================================================
# main.py
# אחריות: תפריט ראשי, קלט מהמשתמש, ניתוב לפונקציות
# ============================================================================
MAIN_MENU = """
=== Soldier Duty Management System ===
1. Add a new soldier
2. Remove a soldier from the system
3. View all soldiers
4. Assign a soldier to a duty
5. Update duty status
6. View a soldier's duties
7. Exit the system
==================================
"""

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
    user_choice = input(f"Enter your choice (1 - {len(MENU_OPTIONS)}): ")
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
    while True:
        try:
            soldier_id = int(input("Enter personal ID: "))
            name = input("Enter name: ")
            add_soldier(soldier_id, name)
            print(f"Soldier -{name}({soldier_id})- added successfully ✓")
            return
        except ValueError as e:
            print(f"""
                ✗ Error: {e}
                Please enter a valid and new ID number!
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
    while True:
        try:
            soldier_id = int(input("Enter personal ID: "))
            remove_soldier(soldier_id)
            print("Soldier removed successfully ✓")
            return
        except ValueError as e:
            print(f"""
                ✗ Error: {e}
                Please enter a valid and existing ID number!
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
        for i, solider in enumerate(solider_list):
            print(f"""
                  {i+1}. -
                  Name - {solider["name"]}
                  ID Number - {solider["id"]}
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
    while True:
        try:
            soldier_id = int(input("Enter personal ID: "))
            duty_name = input("Enter duty name: ")
            day = input("Enter day: ")
            add_duty_to_soldier(soldier_id, duty_name, day)
            print("Duty added successfully ✓")
            return
        except (ValueError, KeyError) as e:
            print(f"""
                ✗ Error: {e}
                Please enter a valid existing ID, a correct duty name, and a valid day of the week!
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
    while True:
        soldier_id = int(input("Enter personal ID: "))
        duty_name = input("Enter duty name: ")
        new_status = input("Enter duty status(pending/completed/missed): ")
        try:
            update_duty_status(soldier_id, duty_name, new_status)
            print("Duty updated successfully ✓")
            return
        except (ValueError, KeyError) as e:
            print(f"""
                ✗ Error: {e}
                Please enter a valid existing ID, a correct duty name, and a valid status!
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
    while True:
        soldier_id = int(input("Enter personal ID: "))
        try:
            soldier_duties = get_soldier_duties(soldier_id)
            if soldier_duties:
                for i, duty in enumerate(soldier_duties):
                    print(f"""{i+1} -
                            Name: {duty["name"]}
                            Day: {duty["day"]}
                            Status: {duty["status"]}
                            """)
            else:
                print("Soldier has no duties.")
            return
        
        except KeyError as e:
            print(f"""
                ✗ Error: {e}
                Please enter a valid and existing ID number!
                """)

def handle_user_exit():
    pass

MENU_OPTIONS = {
    "1": handle_add_soldier,
    "2": handle_remove_soldier,
    "3": handle_view_soldiers,
    "4": handle_add_duty,
    "5": handle_update_duty_status,
    "6": handle_view_soldier_duties,
    "7": handle_user_exit,
}

def main() -> None:
    """
    הפונקציה הראשית של התוכנית.
    מריצה לולאה ראשית שמציגה תפריט, מקבלת בחירה ומפעילה פעולה.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    נקודת הכניסה לתוכנית. מנהלת את הזרימה הראשית.
    """
    print(SOLDIER_ART)
    while True:
        show_menu()
        user_choice = get_user_choice()
        func = MENU_OPTIONS.get(user_choice)
        if func:
            func()
        else:
            print("Enter a valid choice...")

if __name__ == "__main__":
    main()