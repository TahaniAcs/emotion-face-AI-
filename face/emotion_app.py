import cv2
from deepface import DeepFace

cap = cv2.VideoCapture(0) # 0 

# التأكد من أن الكاميرا تعمل
if not cap.isOpened():
    print("لا يمكن الوصول إلى الكاميرا.")
    exit()

while True:
    # قراءة إطار (صورة) من الكاميرا
    ret, frame = cap.read()
    
    # إذا لم يتم قراءة الإطار بنجاح، نخرج من الحلقة
    if not ret:
        break

    try:
        # تحليل الصورة باستخدام DeepFace (الإجراء هو 'emotion')
        # DeepFace سيكتشف الوجه ويحلل المشاعر
        analysis = DeepFace.analyze(
            frame, 
            actions = ['emotion'], 
            enforce_detection=False # يسمح بالتحليل حتى لو كان الوجه غير واضح تمامًا
        )
        
        # استخراج المشاعر الأكثر سيطرة
        emotion = analysis[0]['dominant_emotion']
        
        # وضع نص المشاعر على شاشة العرض
        cv2.putText(frame, emotion, 
                    (50, 50), # موقع النص
                    cv2.FONT_HERSHEY_SIMPLEX, 
                    1, # حجم الخط
                    (0, 255, 0), # لون أخضر
                    2, # سماكة الخط
                    cv2.LINE_AA)
        
    except:
        # إذا لم يتم العثور على وجه، لن يظهر شيء أو رسالة خطأ
        cv2.putText(frame, "Waiting for face...", 
                    (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
        pass

    # عرض الإطار (صورة الكاميرا مع النص)
    cv2.imshow('AI Emotion Mirror', frame)
    
    # الخروج عند الضغط على زر 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# تحرير الكاميرا وإغلاق جميع النوافذ
cap.release()
cv2.destroyAllWindows()