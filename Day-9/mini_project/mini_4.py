import numpy as np
a = np.arange(76,100)
b = a.reshape(2,4,3)
marks = np.concatenate((b,b))
print(marks)
print(marks.shape)
student_avg = np.mean(marks,axis=(1,2))
print(student_avg)
exam_avg = np.mean(marks, axis=(0,1))
print(exam_avg)
top_student = np.argmax(student_avg)
grace_marks = marks+5
grace_marks = np.clip(grace_marks,0,100)
print(grace_marks)
status=np.where(student_avg>=70,'pass','fail')
print(status)
ranks = np.argsort(student_avg)[::-1]
flat_data =  marks.reshape(5,-1)
print(flat_data.shape)
