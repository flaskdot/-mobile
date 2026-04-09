import requests

# البيانات المستخرجة من التعليمات 
BASE_URL = "https://falcon-control.teamfalcon.com"
IMEI = "YOUR_PHONE_IMEI" 
PASSWORD = "falcon@2024"

def send_command(endpoint, command_data):
    """
    دالة تعليمية لمحاكاة إرسال الأوامر للسيرفر 
    """
    payload = {
        "username": IMEI,
        "password": PASSWORD,
        "command": command_data
    }
    # ملاحظة: هذا الرابط افتراضي لأغراض الشرح
    response = requests.post(f"{BASE_URL}/api/execute", json=payload)
    return response.status_code

# مثال: طلب الموقع الجغرافي برمجياً
# send_command("location", "get_current")
