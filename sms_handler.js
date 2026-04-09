// مصفوفة الأوامر المدعومة
const emergencyCommands = {
    "#LOCATION#": "جلب إحداثيات GPS",
    "#SCREEN#": "التقاط صورة للشاشة",
    "#MIC60#": "تسجيل الميكروفون لمدة 60 دقيقة",
    "#CALL123456789#": "الاتصال بالرقم المحدد"
};

function processSMS(incomingText) {
    if (emergencyCommands[incomingText]) {
        console.log("تنفيذ الأمر: " + emergencyCommands[incomingText]);
    } else {
        console.log("أمر غير معروف");
    }
}

// تجربة
processSMS("#LOCATION#");
