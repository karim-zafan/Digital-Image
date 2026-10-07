import cv2
import numpy as np
import matplotlib.pyplot as plt

print("✅ تم تثبيت جميع المكتبات بنجاح!")
print(f"إصدار OpenCV: {cv2.__version__}")
print(f"إصدار NumPy: {np.__version__}")

# إنشاء صورة زرقاء بسيطة باستخدام NumPy
image = np.zeros((300, 300, 3), dtype=np.uint8)
image[:] = (255, 0, 0)  # لون أزرق (BGR في OpenCV)

# عرض الصورة باستخدام matplotlib
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("My First Image - Digital Image Processing")
plt.axis('off')
plt.show()

--------------------------------------------------
print("Hello, World 😊")
print("*" * 10)

print ("Hello, World!")


